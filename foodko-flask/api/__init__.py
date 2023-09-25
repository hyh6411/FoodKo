from .account_ import bp


def _init_blueprint(app):
    app.register_blueprint(bp)
