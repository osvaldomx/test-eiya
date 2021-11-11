"""
Test Eiya
"""
from flask import render_template

from config import DevelopConfig

from services import create_app

from services.models.vehiculo import Vehiculo

app = create_app(DevelopConfig)
title = "Administrador de flotilla"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html",
                            error=error,
                            title=title), 404

@app.route('/')
def index():
    vehiculos = Vehiculo.query.all()
    return render_template("index.html", 
                            vehiculos=vehiculos,
                            title=title), 200

@app.route('/admin')
def admin():
    return render_template("admin.html", title=title), 200

if __name__ == '__main__':
    app.run('0.0.0.0')