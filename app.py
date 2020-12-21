import os
from app import app
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from app.main.models.BaseModel import db

# logger = logging.getLogger(__name__)
ma = Marshmallow(app)
migrate = Migrate(app, db)
""" !*****************************************************************

    Database Models Must be imported here to reflect changes in the DB 

    !*****************************************************************
"""
from app.main.models import user, game, score


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
def test():
    """Run the Unit Tests for the app"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
