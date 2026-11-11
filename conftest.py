"""Config pytest per repo dataset (modello multi-dataset, ADR-001)."""

from __future__ import annotations

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Registra i custom markers a livello di repo (policy test del Lab)."""
    config.addinivalue_line("markers", "pure_unit: pure logic, zero side effects")
    config.addinivalue_line("markers", "contract: public interface, contract API")
    config.addinivalue_line("markers", "smoke: golden path end-to-end")
    config.addinivalue_line("markers", "adapter: external service adapter logic")
    config.addinivalue_line("markers", "regression: bug fix documentato in issue/PR")
    config.addinivalue_line("markers", "policy: regola non ovvia o comportamento cross-component")
