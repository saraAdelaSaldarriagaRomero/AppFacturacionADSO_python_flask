from flask import Flask, render_template

app = Flask(__name__)

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
