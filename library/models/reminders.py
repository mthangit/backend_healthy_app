from ..extensions import db

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __init__(self, content, datetime):
        self.content = content
        self.datetime = datetime