from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all():
    users = UserService.get_all()
    return jsonify([{
        'id': user.id,
        'name': user.username,
        '': user.email
    } for user in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400
    new_user = UserService.create_resource(data)
    return jsonify({
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email
    }), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_user = UserService.update_resource(user_id, data)
    if not updated_user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({
        'id': updated_user.id,
        'username': updated_user.username,
        'email': updated_user.email
    }), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_user = UserService.delete_resource(user_id)
    if not deleted_user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({'message': 'Usuario eliminado'}), 200
