# May 21

Screw it, I'm adding a `package.json` to get Prettier on Markdown. Don't hate me. I'll make a `.gitignore` and keep that
out of the repo.

Themester and Goku had a system where you could put a function in your `conf.py`. If present, `builder-init` would call
it with the registry, and you could add stuff conveniently, just for your project. Let's bring that over, with tests.
This probably will be a common pattern for all Themester-supported targets. We will make the function `svcs_setup`. It
will be invoked last, after Sphinx stuff is added to the registry. I'll start by adding something to
`test-sphinx-svcs-setup` that fails.

# May 20

Get started with a `uv init` targeting 3.10 or higher.

Get Sphinx test roots setup with pytest and conftest.py. I took a look at what's in Sphinx for the fixtures, but also
copied over some of my previous work. I started with my BeautifulSoup fixtures, but I'm not really going to be testing
HTML output, so simplify the dependencies.

Start some Sphinx setup functions to wire in builder-inited and get tests that find the registry in the SphinxTestApp.

We name the svcs registry as app.site_registry to avoid conflicting with Sphinx's app.registry.
