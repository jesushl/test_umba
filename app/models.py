from main import app

db = app.db

class Coder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    avatar = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(5), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "{self.username} {self.user}"
