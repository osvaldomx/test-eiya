"""
Test Eiya
"""
from flask import Blueprint
from flask import request

from ..models.vehiculo import Vehiculo
from ..models.vehiculo import VehiculoSchema

from ..utils.responses import bad_request, response

vehiculo = Blueprint('vehiculos', __name__)

@vehiculo.route('/vehiculos')
@vehiculo.route('/vehiculos/all')
def get_all():
    vehiculos = Vehiculo.query.all()

    if vehiculos:
        return response(VehiculoSchema(many=True).dump(vehiculos))

    return bad_request()

@vehiculo.route('/vehiculos/<int:id>')
def get_by_id(id):
    vehiculo = Vehiculo.query.filter_by(vehiculo_id=id).first()
    if vehiculo:
        return response(VehiculoSchema().dump(vehiculo))

    return bad_request()

@vehiculo.route('/vehiculos/crear', methods=['POST'])
def crear_vehiculo():
    data = request.get_json(force=True)
    vehiculo = Vehiculo(
        data['id'],
        data['ubicacion'],
        data['consumo'],
        data['distancia'],
        data['combustible']
    )

    if vehiculo.save():
        return response(VehiculoSchema().dump(vehiculo))

    return bad_request()

@vehiculo.route('/vehiculos/edit/<int:id>', methods=['PUT'])
def edit_vehiculo(id):
    data = request.get_json(force=True)
    vehiculo = Vehiculo.query.filter_by(vehiculo_id=id).first()
    vehiculo.vehiculo_ubicacion_actual = data['ubicacion']
    vehiculo.vehiculo_consumo_combustible = data['consumo']
    vehiculo.vehiculo_distancia_recorrida = data['distancia']
    vehiculo.vehiculo_combustible_consumido = data['combustible']

    if vehiculo.edit():
        return response(VehiculoSchema().dump(vehiculo))

    return bad_request()

@vehiculo.route('/vehiculos/eliminar/<int:id>', methods=['DELETE'])
def eliminar_vehiculo(id):
    vehiculo = Vehiculo.query.filter_by(vehiculo_id=id).first()

    if vehiculo.delete():
        return response("Vehicle {} deleted".format(id))
    
    return bad_request()

@vehiculo.route('/vehiculos/viaje', methods=['POST'])
def crear_viaje():
    distances = {
        'A': {'B': 1, 'C': 2}, 
        'B': {'A': 1, 'C': 4}, 
        'C': {'A': 2, 'B': 4}
    }
    data = request.get_json(force=True)
    vehiculo = Vehiculo.query.filter_by(vehiculo_id=data['id']).first()

    origen = data['origen'].split(' ')[-1]
    destino = data['destino'].split(' ')[-1]
    distancia = distances[origen][destino]
    combustible = distancia / vehiculo.vehiculo_consumo_combustible

    vehiculo.vehiculo_ubicacion_actual = data['destino']
    vehiculo.vehiculo_distancia_recorrida += distancia
    vehiculo.vehiculo_combustible_consumido += combustible

    if vehiculo.edit():
        return response(VehiculoSchema().dump(vehiculo))

    return bad_request()
