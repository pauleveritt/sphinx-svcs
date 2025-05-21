"""Sphinx config file for this test."""

from svcs import Registry

project = "sphinx-setup"
extensions = ["sphinx_svcs"]
# here = Path(__file__)


def svcs_setup(registry: Registry):
    """Customize the registry for this site."""

    registry.register_value(IndentationError, "Fake the IndentationError")
