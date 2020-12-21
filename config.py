import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DB_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'Development': DevelopmentConfig,
    'Testing': TestingConfig,
    'Production': ProductionConfig,
    'Default': DevelopmentConfig,
    'Deploy': DeploymentConfig
}
