from flask import Flask

import settings
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app)
    app.register_blueprint(user_bp)

    return app
