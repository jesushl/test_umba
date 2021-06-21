import os
class Config:
    SECRET_KEY = "UBUNTU"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = database = os.environ.get(
        'DATABASE_URL',
        "sqlite:///main/database/git_hub_test.db"
    )
    if os.environ.get()
    SQLALCHEMY_TRACK_MODIFICATIONS=True
