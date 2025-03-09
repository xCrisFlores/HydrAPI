from app import db
from app.models import RealTimeCon

class ConsumptionService:
    @staticmethod
    def get_all():
        return RealTimeCon.query.all()

    @staticmethod
    def get_by_id(id):
        return RealTimeCon.query.get(id)

    @staticmethod
    def create_resource(data):
        new_consumption = RealTimeCon(
            consumption = data["consumption"],
            time_active = data["time_active"],
            date = data["date"],
            user_id = data["user_id"],
            sensor_id = data["sensor_id"]
        )

        db.session.add(new_consumption)
        db.session.commit()
        return new_consumption

