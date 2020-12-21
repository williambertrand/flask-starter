import logging

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)

# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize Marshmallow
ma = Marshmallow()

# For pagination purposes, we will return at most MAX_NUMBER_OF_RECORDS_TO_FETCH
MAX_NUMBER_OF_RECORDS_TO_FETCH = 100


# ------------------ #
#    Base Entity     #
# ------------------ #
class Entity(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_by = db.Column(db.Integer)