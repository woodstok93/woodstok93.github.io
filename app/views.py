from flask import jsonify, request
from app.models import Reservas
from flask import jsonify, request
 

def index():
    return jsonify({'message': 'Hello World API '})

def create_Reservas():
    data = request.json
    new_reservas = Reservas(email=data['email'], nombre=data['nombre'], mensaje=data['mensaje'], id=data['id'])
    new_reservas.save()
    return jsonify({'message': 'Reservas created successfully'}), 201

def get_all_reservas():
    reservas = Reservas.get_all()
    return jsonify([reservas.serialize() for reservas in reservas])

def get_reservas(reservas_id):
    reservas = Reservas.get_by_id(reservas_id)
    if not reservas:
        return jsonify({'message': 'reservas not found'}), 404
    return jsonify(reservas.serialize())

def update_movie(reservas_id):
    reservas = Reservas.get_by_id(reservas_id)
    if not reservas:
        return jsonify({'message': 'Reservas not found'}), 404
    data = request.json
    reservas.title = data['Email']
    reservas.director = data['Nombre']
    reservas.release_date = data['Mensaje']
    reservas.banner = data['id']
    reservas.save()
    return jsonify({'message': 'Reservas updated successfully'})

def delete_movie(reservas_id):
    reservas = Reservas.get_by_id(reservas_id)
    if not Reservas:
        return jsonify({'message': 'Reservas not found'}), 404
    Reservas.delete()
    return jsonify({'message': 'Reservas deleted successfully'}) 
 