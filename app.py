
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



@app.route('/crear_producto', methods=['POST','GET'])
def crear_producto():    
    if request.method == 'POST':
        descripcion = request.form.get('descripcion')    
        valor_unitario = request.form.get('valor_unitario')    
        unidad_medida = request.form.get('unidad_medida')    
        cantidad_stock = request.form.get('cantidad_stock')    
        categoria = request.form.get('categoria')    
        producto = Productos(descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria)
        Productos.agregar_producto(producto)
        return redirect(url_for('ver_productos'))
    categorias = Categorias.obtener_categorias()
    return render_template('formulario_crear_producto.html', titulo_pagina = 'Crear Producto', categorias=categorias)


@app.route('/ver_productos')
def ver_productos():
    productos = Productos.obtener_productos()
    return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)




@app.route('/crear_cliente', methods=['POST', 'GET'])
def crear_cliente():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_completo = request.form.get('nombre_completo')
        direccion = request.form.get('direccion')
        fecha_nacimiento = request.form.get('fecha_nacimiento')  # Formato YYYY-MM-DD
        telefono = request.form.get('telefono')

        # Crear una instancia de Clientes
        cliente = Clientes(
            nombre_completo=nombre_completo,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono
        )
        
        # Guardar el cliente en la base de datos
        Clientes.agregar_clientes(cliente)
        
        # Redirigir a la página para ver clientes
        return redirect(url_for('ver_clientes'))
    
    return render_template('formulario_crear_cliente.html', titulo_pagina='Crear Cliente')

@app.route('/ver_clientes')
def ver_clientes():
    # Obtener todos los clientes de la base de datos
    clientes = Clientes.obtener_clientes()
    
    # Renderizar la plantilla con la lista de clientes
    return render_template('tabla_clientes.html', titulo_pagina='Ver Clientes', clientes=clientes)












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
