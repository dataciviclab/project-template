"""Smoke test — verifica che tutte le pagine si compilano senza errori."""

from __future__ import annotations

import py_compile
from pathlib import Path

import pytest

pytestmark = pytest.mark.smoke

DASHBOARD_DIR = Path(__file__).resolve().parent.parent
PAGES_DIR = DASHBOARD_DIR / "pages"


def test_app_compiles() -> None:
    """L'entry point (branding + navigazione) deve compilarsi."""
    py_compile.compile(str(DASHBOARD_DIR / "app.py"), doraise=True)


@pytest.mark.parametrize(
    "page",
    sorted(PAGES_DIR.glob("*.py")),
    ids=lambda p: p.stem,
)
def test_page_compiles(page: Path) -> None:
    """Ogni pagina deve compilarsi senza errori di sintassi."""
    py_compile.compile(str(page), doraise=True)
