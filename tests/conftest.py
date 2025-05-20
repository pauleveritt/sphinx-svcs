from pathlib import Path
from typing import Any, Generator

import pytest
from sphinx.testing.util import SphinxTestApp

pytest_plugins = ('sphinx.testing.fixtures',)

_TESTS_ROOT = Path(__file__).resolve().parent
_ROOTS_DIR = _TESTS_ROOT / 'roots'


@pytest.fixture(scope='session')
def rootdir() -> Path:
    return _ROOTS_DIR


@pytest.fixture()
def content(app: SphinxTestApp) -> Generator[SphinxTestApp, Any, None]:
    """The content generated from a Sphinx site."""
    app.build()
    yield app



@pytest.fixture()
def page(content: SphinxTestApp, request) -> Generator[Any, Any, None]:
    """Get the text for a page and convert to BeautifulSoup document."""
    pagename = request.param
    yield (content.outdir / pagename).read_text()

