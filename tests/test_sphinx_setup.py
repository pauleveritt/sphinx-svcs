"""Integration test for Sphinx themester with no theme."""
import pytest

pytestmark = pytest.mark.sphinx("html", testroot="sphinx-setup")


@pytest.mark.parametrize(
    "page",
    [
        "index.html",
    ],
    indirect=True,
)
def test_index(page: str) -> None:
    """Ensure basics are in the page."""
    assert "sphinx-setup" in page
