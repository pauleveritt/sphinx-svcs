"""Test the outermost extension setup."""

import pytest
from sphinx.testing.util import SphinxTestApp
from svcs import Registry, Container
from venusian import Scanner

from sphinx_svcs import setup as extension_setup
from sphinx_svcs.builder_init import setup as builder_init_setup
from sphinx.application import (
    Sphinx,
    Config as SphinxConfig,
    BuildEnvironment as SphinxBuildEnvironment,
)

pytestmark = pytest.mark.sphinx("html", testroot="sphinx-svcs-setup")


def test_setup(app: SphinxTestApp):
    extension_setup(app)
    assert getattr(app, "site_registry")


def test_builder_init(app: SphinxTestApp):
    builder_init_setup(app)
    site_registry: Registry = getattr(app, "site_registry")
    container = Container(registry=site_registry)
    sphinx_app = container.get(Sphinx)
    assert isinstance(sphinx_app, SphinxTestApp)
    sphinx_config = container.get(SphinxConfig)
    assert isinstance(sphinx_config, SphinxConfig)
    sphinx_build_env = container.get(SphinxBuildEnvironment)
    assert isinstance(sphinx_build_env, SphinxBuildEnvironment)
    venusian_scanner = container.get(Scanner)
    assert isinstance(venusian_scanner, Scanner)
    assert getattr(venusian_scanner, "site_registry")


def test_svcs_setup(app: SphinxTestApp):
    """See if test-sphinx-svcs-setup conf.py has a customization function."""
    builder_init_setup(app)
    site_registry: Registry = getattr(app, "site_registry")
    container = Container(registry=site_registry)
    assert IndentationError
    fake_windows_error = container.get(IndentationError)
    assert fake_windows_error == "Fake the IndentationError"
