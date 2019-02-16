from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)
    db.init_app(app)
    migrate = Migrate(app, db)
    from counter.views import counter_app
    app.register_blueprint(counter_app)
    return app
