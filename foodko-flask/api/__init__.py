from .account_ import bp
from .question_list import question_bp
from .chemical_element import element_bp
from .ingredients_list import ingredients_bp
from .food_list import food_dp
from .record_list import record_bp
from .public import public_bp


def _init_blueprint(app):
    app.register_blueprint(bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(element_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(food_dp)
    app.register_blueprint(record_bp)
    app.register_blueprint(public_bp)

