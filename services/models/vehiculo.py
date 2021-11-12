"""
Test Eiya
"""
from . import db

from marshmallow import Schema
from marshmallow import fields

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'

    vehiculo_id = db.Column(db.Integer, primary_key=True)
    vehiculo_ubicacion_actual = db.Column(db.String(20), nullable=False)
    vehiculo_consumo_combustible = db.Column(db.Integer)
    vehiculo_distancia_recorrida = db.Column(db.Integer, nullable=False)
    vehiculo_combustible_consumido = db.Column(db.Float, nullable=False)

    def __init__(self, id, ubicacion, consumo, distancia, combustible) -> None:
        self.vehiculo_id = id
        self.vehiculo_ubicacion_actual = ubicacion
        self.vehiculo_consumo_combustible = consumo
        self.vehiculo_distancia_recorrida = distancia
        self.vehiculo_combustible_consumido = combustible

    def save(self) -> bool:
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def edit(self) -> bool:
        try:
            db.session.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def delete(self) -> bool:
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

class VehiculoSchema(Schema):
    vehiculo_id = fields.Int()
    vehiculo_ubicacion_actual = fields.Str()
    vehiculo_consumo_combustible = fields.Int()
    vehiculo_distancia_recorrida = fields.Int()
    vehiculo_combustible_consumido = fields.Decimal()
