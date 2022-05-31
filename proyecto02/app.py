"""
    Tomado de https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
"""

import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))
from config import enlace
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = enlace 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Matricula(db.Model):

    __tablename__ = 'matriculas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    placa = db.Column(db.String(200))
    anio = db.Column(db.Integer)
    costo = db.Column(db.Integer, nullable=False) # este atributo no puede ser nulo


    def __repr__(self):
        return "Matricula: nombre=%s placa=%s anio:%s costo:%s" % (
                          self.nombre,
                          self.placa,
                          self.anio,
                          self.costo)

# vista

@app.route('/')
def index():
    matriculas = Matricula.query.all()
    return render_template('index.html', matriculas=matriculas)


@app.route('/<int:matricula_id>/')
def matricula(matricula_id):
    matricula = Matricula.query.get_or_404(matricula_id)
    return render_template('matricula.html', matricula=matricula)


@app.route('/add/matricula/', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']
        m = Matricula(nombre=nombre,
                          placa=placa,
                          anio=anio,
                          costo=costo
                          )
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/matricula/<int:matricula_id>/', methods=('GET', 'POST'))
def editar(matricula_id):
    matricula = Matricula.query.get_or_404(matricula_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']

        matricula.nombre = nombre
        matricula.placa = placa
        matricula.anio = anio
        matricula.costo = costo
        db.session.add(matricula)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', matricula=matricula)
