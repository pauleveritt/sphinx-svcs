"""Services for the builder init Sphinx event."""

from sphinx.application import (
    Sphinx,
    Config as SphinxConfig,
    BuildEnvironment as SphinxBuildEnvironment,
)

from svcs import Registry
from venusian import Scanner


def setup(app: Sphinx) -> None:
    """Handle the Sphinx ``builder_init`` event."""
    site_registry = Registry()
    setattr(app, "site_registry", site_registry)  # noqa: B010

    # Add the external data from Sphinx class instances
    site_registry.register_value(Sphinx, app)
    site_registry.register_value(SphinxConfig, app.config)
    site_registry.register_value(SphinxBuildEnvironment, app.env)

    # Make a Venusian scanner and put it in the registry. Also, put
    # the registry on the scanner so decorators can get to it, and
    # thus get to sphinx_app etc.
    scanner = Scanner(site_registry=site_registry)
    site_registry.register_value(Scanner, scanner)

    # Look in conf.py for a `svcs_setup` function
    raw_config = getattr(app.config, "_raw_config")
    svcs_setup = raw_config.get("svcs_setup", None)
    if svcs_setup is not None:
        svcs_setup(site_registry)

    # # Sphinx wants _static instead of static
    # static_dest = StaticDest(dest=PurePosixPath("_static"))
    # site_registry.register(static_dest)
