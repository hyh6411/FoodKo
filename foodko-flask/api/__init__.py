from .account_ import bp
from .question_list import question_bp
from .chemical_element import element_bp


def _init_blueprint(app):
    app.register_blueprint(bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(element_bp)
