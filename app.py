"""
Test Eiya
"""
from datetime import datetime

from flask import render_template
from flask import request
from flask import flash

from config import DevelopConfig

from services import create_app

from services.models.vehiculo import Vehiculo

from services.utils.forms import BasicForm
from services.utils.forms import TripForm

from services.models import db

app = create_app(DevelopConfig)
TITLE = "Administrador de flotilla"

@app.errorhandler(404)
def page_not_found(error):
    """
    """
    return render_template("404.html",
                            error=error,
                            title=TITLE), 404

@app.route('/')
def index():
    """
    """
    vehiculos = Vehiculo.query.all()
    return render_template("index.html",
                            vehiculos=vehiculos,
                            title=TITLE), 200

@app.route('/admin', methods=["GET", "POST"])
def admin():
    """
    """
    distances = {'A': [0, 1, 2],
                    'B': [1, 0, 4],
                    'C': [2, 4, 0]}

    create_form = BasicForm(request.form)

    edit_form = BasicForm(request.form)
    edit_form.method = "put"

    delete_form = BasicForm(request.form)
    delete_form.method = "delete"

    trip_form = TripForm(request.form)
    objs = Vehiculo.query.all()
    trip_form.id.choices = [(o.vehiculo_id, o.vehiculo_id) for o in objs]

    if request.method == "POST" and\
            request.form.get('_method') == "post" and\
            create_form.validate():
        vehiculo = Vehiculo(
            create_form.id.data,
            create_form.ubicacion.data,
            create_form.consumo.data,
            create_form.distancia.data,
            create_form.combustible.data
        )

        try:
            db.session.add(vehiculo)
            db.session.commit()
            flash("Vehículo creado exitosamente!")
        except Exception as exc:
            raise exc

    if request.method == "POST" and\
            request.form.get('_method') == "put" and\
            edit_form.validate():
        obj_update = Vehiculo.query.filter_by(vehiculo_id=edit_form.id.data).first()
        obj_update.vehiculo_ubicacion_actual = edit_form.ubicacion.data
        obj_update.vehiculo_consumo_combustible = edit_form.consumo.data
        obj_update.vehiculo_distancia_recorrida = edit_form.distancia.data
        obj_update.vehiculo_combustible_consumido = edit_form.combustible.data

        try:
            db.session.commit()
            flash("Vehículo actualizado exitosamente!")
        except Exception as exc:
            raise exc

    if request.method == "POST" and\
            request.form.get('_method') == 'delete':
        obj_delete = Vehiculo.query.filter_by(vehiculo_id=delete_form.id.data).first()
        try:
            db.session.delete(obj_delete)
            db.session.commit()
            flash("Vehículo eliminado exitosamente!")
        except Exception as exc:
            raise exc

    if request.method == "POST" and\
            request.form.get('_method') == 'create':
        vid = trip_form.id.data
        origen = trip_form.origen.data
        destino = int(trip_form.destino.data)
        distancia = distances[origen][destino]

        vehiculo = Vehiculo.query.filter_by(vehiculo_id=vid).first()

        distancia_total = vehiculo.vehiculo_distancia_recorrida + distancia
        combustible = distancia / vehiculo.vehiculo_consumo_combustible
        combustible_total = vehiculo.vehiculo_combustible_consumido + combustible

        vehiculo.vehiculo_ubicacion_actual = "CIUDAD " + list(distances.keys())[destino]
        vehiculo.vehiculo_distancia_recorrida = distancia_total
        vehiculo.vehiculo_combustible_consumido = combustible_total

        try:
            db.session.commit()
            return render_template("details.html",
                                    title=TITLE,
                                    id=vid,
                                    origen=origen,
                                    destino=list(distances.keys())[destino],
                                    distancia=distancia,
                                    combustible=combustible,
                                    obj=vehiculo,
                                    date=datetime.now().strftime("%d-%m-%Y %H:%M")
                                    ), 200
        except Exception as exc:
            raise exc

    return render_template("admin.html",
                            title=TITLE,
                            create=create_form,
                            edit=edit_form,
                            delete=delete_form,
                            trip=trip_form), 200

if __name__ == '__main__':
    app.run()
