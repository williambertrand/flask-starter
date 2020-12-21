from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from config import config
from environs import Env
from app.main.models.BaseModel import db
from flask_cors import CORS


mail = Mail()
moment = Moment()

env = Env()
env.read_env()

version_prefix = 'v0.1'


def create_app(env_name=None):
    app = Flask(__name__)
    CORS(app)
    if not env_name:
        env_name = env('FLASK_ENV', 'Development')
    app.config.from_object(config[env_name])
    config[env_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from .main import models

    from .main import main_bp as main_blueprint
    from .main.endpoints.users import users
    #TODO: Import Game BP

    app.register_blueprint(main_blueprint)
    app.register_blueprint(users.users_bp)

    return app

app = create_app()
