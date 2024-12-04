from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    sensors = db.relationship('Sensor', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    real_time_cons = db.relationship('RealTimeCon', backref='sensor', lazy=True)

    def __repr__(self):
        return f'<Sensor {self.name}>'

class RealTimeCon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumption = db.Column(db.Float, nullable=False)
    time_active = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

    def __repr__(self):
        return f'<RealTimeCon {self.consumption} kWh at {self.date}>'
