from flask import Flask, render_template
# Importa la clase Flask desde el módulo flask.
# Flask es un micro framework utilizado para crear aplicaciones web en Python.

app = Flask(__name__)
# Crea una instancia de la aplicación Flask.
# __name__ es una variable especial en Python que representa el nombre del módulo actual.
# Esto ayuda a Flask a identificar la ubicación de los recursos como plantillas y archivos estáticos.

if __name__ == '__main__':
# La comparación __name__ == '__main__' se utiliza para verificar si el script está siendo ejecutado directamente.
# Si es así, el bloque de código dentro de este condicional se ejecutará.

    app.run(debug=True)
    # Inicia la aplicación Flask con el servidor integrado.
    # El parámetro debug=True activa el modo de depuración, lo que permite reiniciar el servidor automáticamente
    # cuando se detectan cambios en el código y proporciona información detallada sobre errores.
@app.route('/')
def index():
    return render_template('index.html',varTituloPagina='Inicio')


@app.route('/productos',varTituloPagina='Productos')
def productos():
    return render_template('productos.html')


@app.route('/clientes',varTituloPagina='Clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/personal')
def personal():
    return render_template('personal.html',varTituloPagina='Personal')

@app.route('/facturas')
def facturas():
    return render_template('facturas.html',varTituloPagina='Facturas')