from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class PublishItem:
    source: Path
    destination: Path


def load_config(config_path: Path) -> dict:
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def resolve_output_root(config_path: Path, cfg: dict) -> Path:
    root_value = cfg.get("root", ".")
    return (config_path.parent / root_value).resolve()


def year_values(cfg: dict, selected_year: int | None) -> list[int]:
    years = cfg["dataset"]["years"]
    if selected_year is None:
        return years
    if selected_year not in years:
        raise ValueError(f"Year {selected_year} not found in dataset.yml years: {years}")
    return [selected_year]


def latest_run_record(run_dir: Path) -> Path | None:
    if not run_dir.exists():
        return None
    candidates = sorted(run_dir.glob("*.json"))
    return candidates[-1] if candidates else None


def build_publish_items(
    *,
    output_root: Path,
    dataset: str,
    years: list[int],
    drive_root: Path,
) -> list[PublishItem]:
    items: list[PublishItem] = []

    for year in years:
        year_text = str(year)
        mart_dir = output_root / "data" / "mart" / dataset / year_text
        clean_dir = output_root / "data" / "clean" / dataset / year_text
        raw_dir = output_root / "data" / "raw" / dataset / year_text
        runs_dir = output_root / "data" / "_runs" / dataset / year_text

        for path in sorted(raw_dir.glob("*")):
            if path.is_file():
                items.append(PublishItem(path, drive_root / path.relative_to(output_root)))

        for path in sorted(mart_dir.glob("*.parquet")):
            items.append(PublishItem(path, drive_root / path.relative_to(output_root)))

        clean_parquet = clean_dir / f"{dataset}_{year_text}_clean.parquet"
        if clean_parquet.exists():
            items.append(PublishItem(clean_parquet, drive_root / clean_parquet.relative_to(output_root)))

        for layer_dir, validation_rel in (
            (raw_dir, "raw_validation.json"),
            (clean_dir, "_validate/clean_validation.json"),
            (mart_dir, "_validate/mart_validation.json"),
        ):
            for name in ("metadata.json", "manifest.json"):
                path = layer_dir / name
                if path.exists():
                    items.append(PublishItem(path, drive_root / path.relative_to(output_root)))

            validation_path = layer_dir / validation_rel
            if validation_path.exists():
                items.append(PublishItem(validation_path, drive_root / validation_path.relative_to(output_root)))

        latest_run = latest_run_record(runs_dir)
        if latest_run is not None:
            items.append(PublishItem(latest_run, drive_root / latest_run.relative_to(output_root)))

    return items


def copy_items(items: list[PublishItem], *, dry_run: bool) -> tuple[int, int]:
    copied = 0
    missing = 0

    for item in items:
        if not item.source.exists():
            print(f"MISSING {item.source}")
            missing += 1
            continue

        print(f"{'DRY-RUN' if dry_run else 'COPY'} {item.source} -> {item.destination}")
        if not dry_run:
            item.destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.source, item.destination)
        copied += 1

    return copied, missing


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Publish dataset artifacts to Drive preserving toolkit output paths under root."
    )
    parser.add_argument("--config", default="dataset.yml", help="Path to dataset.yml")
    parser.add_argument("--drive-root", required=True, help="Destination root in Drive")
    parser.add_argument("--year", type=int, help="Publish a single year")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be copied without writing")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config_path = Path(args.config).resolve()
    cfg = load_config(config_path)

    dataset = cfg["dataset"]["name"]
    years = year_values(cfg, args.year)
    output_root = resolve_output_root(config_path, cfg)
    drive_root = Path(args.drive_root).resolve()

    items = build_publish_items(
        output_root=output_root,
        dataset=dataset,
        years=years,
        drive_root=drive_root,
    )

    print(
        {
            "dataset": dataset,
            "years": years,
            "output_root": str(output_root),
            "drive_root": str(drive_root),
            "dry_run": args.dry_run,
            "items": len(items),
        }
    )

    copied, missing = copy_items(items, dry_run=args.dry_run)
    print({"copied": copied, "missing": missing})
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
