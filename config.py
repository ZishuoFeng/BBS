import os

SECRET_KEY = os.urandom(24)

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:glorious654@localhost/bbs_rectify"
SQLALCHEMY_TRACK_MODIFICATIONS = True
