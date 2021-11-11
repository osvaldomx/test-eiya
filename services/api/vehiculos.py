"""
Test Eiya
"""
from flask import Blueprint

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

@vehiculo.route('/vehiculos/crear', methods=['POST'])
def crear_vehiculo():
    pass
