from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    value = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.String(30), nullable=False)
    isElectronic = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, value, creation_date, isElectronic):
        self.name = name
        self.value = value
        self.creation_date = creation_date
        self.isElectronic = isElectronic

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "creation_date": self.creation_date,
            "isElectronic": self.isElectronic
        }
