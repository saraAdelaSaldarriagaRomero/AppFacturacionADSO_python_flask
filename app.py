
from flask import Flask, render_template, request, redirect, url_for
from models import Base, engine
from models.productos import Productos
from models.categorias import Categorias
from models.personal import Personal
from models.clientes import Clientes

app = Flask(__name__)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html', varTituloPagina='Inicio')

@app.route('/productos')
def productos():
    return render_template('productos.html', varTituloPagina='Productos')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', varTituloPagina='Clientes')

@app.route('/personal')
def personal():
    return render_template('personal.html', varTituloPagina='Personal')

@app.route('/facturas')
def facturas():
    return render_template('facturas.html', varTituloPagina='Facturas')

if __name__ == '__main__':
    app.run(debug=True)
