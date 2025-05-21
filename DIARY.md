May 20
======

Get started with a `uv init` targeting 3.10 or higher.

Get Sphinx test roots setup with pytest and conftest.py. I took a look at what's in Sphinx for the fixtures, but also
copied over some of my previous work. I started with my BeautifulSoup fixtures, but I'm not really going to be testing
HTML output, so simplify the dependencies.

Start some Sphinx setup functions to wire in builder-inited and get tests that find the registry in the SphinxTestApp.