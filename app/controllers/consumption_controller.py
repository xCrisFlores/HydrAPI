from flask import Blueprint, jsonify, request
from app.services.consumption_service import ConsumptionService

consumption_bp = Blueprint('consumption_bp', __name__)

@consumption_bp.route('/consumption', methods=['GET'])
def get_all():
    consumptions = ConsumptionService.get_all()
    return jsonify([{
        'id': consumption.id,
        'consumption': consumption.consumption,
        'time_active': consumption.time_active,
        'date': consumption.date.isoformat(),
        'user_id': consumption.user_id,
        'sensor_id': consumption.sensor_id
    } for consumption in consumptions]), 200

@consumption_bp.route('/consumption/<int:id>', methods=['GET'])
def get_consumption(id):
    consumption = ConsumptionService.get_by_id(id)
    if not consumption:
        return jsonify({'error': 'Consumo no encontrado'}), 404
    return jsonify({
        'id': consumption.id,
        'consumption': consumption.consumption,
        'time_active': consumption.time_active,
        'date': consumption.date.isoformat(),
        'user_id': consumption.user_id,
        'sensor_id': consumption.sensor_id
    }), 200

@consumption_bp.route('/consumption', methods=['POST'])
def create_consumption():
    try:
        data = request.get_json()

        required_fields = ['consumption', 'time_active', 'date', 'user_id', 'sensor_id']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        try:
            new_consumption = ConsumptionService.create_resource(data)
        except Exception as e:
            return jsonify({'error': 'Error al guardar en la base de datos'}), 500

        return jsonify({
            'id': new_consumption.id,
            'consumption': new_consumption.consumption,
            'time_active': new_consumption.time_active,
            'date': new_consumption.date.isoformat(), 
            'user_id': new_consumption.user_id,
            'sensor_id': new_consumption.sensor_id
        }), 201

    except Exception as e:
        print(f"Error inesperado: {e}") 
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500