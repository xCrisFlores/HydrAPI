from app import db
from app.models import Sensor

class SensorService:
    @staticmethod
    def get_all():
        return Sensor.query.all()

    @staticmethod
    def get_by_id(id):
        return Sensor.query.get(id)

    @staticmethod
    def create_resource(data):
        new_sensor = Sensor(
            name = data["name"],
            user_id = data["user_id"],
        )

        db.session.add(new_sensor)
        db.session.commit()
        return new_sensor

    @staticmethod
    def update_resource(id, data):
        sensor = Sensor.query.get(id)
        if not sensor:
            return None
        sensor.name = data.get('name', sensor.name)
        db.session.commit()
        return sensor

    @staticmethod
    def delete_resource(id):
        sensor = Sensor.query.get(id)
        if not sensor:
            return None
        db.session.delete(sensor)
        db.session.commit()
        return sensor
