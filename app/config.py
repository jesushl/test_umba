import os


class Config:
    SECRET_KEY = "UBUNTU"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL'
    )
    if not SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = "sqlite:///main/database/git_hub_test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
