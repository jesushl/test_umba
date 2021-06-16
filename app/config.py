class Config:
    SECRET_KEY = "UBUNTU"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///main/database/git_hub_test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
