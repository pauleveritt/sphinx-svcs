from sphinx_svcs import builder_init


def setup(app):
    # app.config.template_bridge = "goku.sphinx_support.TemplateBridge"
    app.connect("builder-inited", builder_init.setup)

    # Put current_document = sphinx_app.env.current_document in the container
    # app.connect("html-page-context", html_page_context)
    # app.connect("html-collect-pages", html_collect_pages)
    # app.connect("build-finished", builder_finished)
