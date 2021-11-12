"""
Test Eiya!
"""
from wtforms import Form
from wtforms import IntegerField
from wtforms import FloatField
from wtforms import SelectField
from wtforms import validators
from wtforms import HiddenField

from ..models.vehiculo import Vehiculo

class BasicForm(Form):
    method = "post"
    _method = HiddenField("", default=method)

    id = IntegerField("ID del vehículo", [
            validators.DataRequired(message="El id del vehículo es requerido."),
            validators.number_range(min=1, message="Ingrese un id válido")
    ])

    ubicacion = SelectField("Ubicación actual", [
        validators.DataRequired(message="La ubicación actual del vehículo es requerida.")
    ], choices=
        [
            ("CIUDAD A", "Ciudad A"),
            ("CIUDAD B", "Ciudad B"),
            ("CIUDAD C", "Ciudad C")
    ])

    consumo = IntegerField("Consumo de combustible (km/lt)", [
        validators.DataRequired(message="El consumo de combustible es requerido."),
        validators.number_range(min=1)
    ])

    distancia = IntegerField("Distancia recorrida", [
        validators.DataRequired("La distancia recorrida es requerida."),
        validators.number_range(min=0)
    ])

    combustible = FloatField("Combustible consumido", [
        validators.DataRequired("El combustible consumido es requerido."),
        validators.number_range(min=0)
    ])

class TripForm(Form):
    method = "create"
    _method = HiddenField("", default=method)

    id = SelectField("ID del vehículo", coerce=int)

    origen = SelectField("Origen del viaje", choices=[
        ("A", "Ciudad A"),
        ("B", "Ciudad B"),
        ("C", "Ciudad C")
    ])
    
    destino = SelectField("Destino del viaje", choices=[
        (0, "Ciudad A"),
        (1, "Ciudad B"),
        (2, "Ciudad C")
    ])