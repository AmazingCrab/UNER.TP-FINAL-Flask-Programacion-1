from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


global opcion_menu_ppal , opcion_menu_vechiculos ,opcion_menu_clientes, opcion_menu_ppal_transaccion 

global h1, h2

h1 = 'Concesionario La Ñata'
h2 = 'Bienvenido!'

@app.route('/', methods=['GET', 'POST'])
def index():
    lista_menu = [
    '1. Vehículos',
    '2. Clientes', 
    '3. Transacciones', 
    '4. Ver Cotización del Dolar', 
    '5. Salir', 
    'Menú Principal',
    'Ir al Menú',h1, h2]   
     
    opcion_menu_ppal = request.form.get('opcion')
    
    return render_template('index.html', **{'lista_menu': lista_menu})

@app.route('/vehiculos', methods=['GET', 'POST'])
def vehiculos():
    lista_menu = ['1. Crear Vehículos', 
    '2. Editar Vehículos', 
    '3. Eliminar Vehículo', 
    '4. Listar Vehículo', 
    '5. Buscar Vehículo',
    '6. Volver al Menú Principal',
    'Menu Vehiculos',
    'Ir al Menú',h1, h2]

    opcion_menu_vehiculos = request.form.get('opcion')

    return render_template('vehiculos.html', **{'lista_menu': lista_menu})

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    lista_menu = [
    '1. Crear Cliente', 
    '2. Editar Cliente', 
    '3. Eliminar Cliente', 
    '4. Listar Clientes', 
    '5. Buscar Clientes', 
    '6. Volver al Menu Principal',
    'Menu Clientes',
    'Ir al Menú',h1, h2]

    opcion_menu_clientes = request.form.get('opcion')

    return render_template('clientes.html', **{'lista_menu': lista_menu})

@app.route('/transacciones', methods=['GET', 'POST'])
def transacciones():
    lista_menu = [
    '1. Crear Transacción', 
    '2. Listar Transacciones',
    '3. Buscar Transacción', 
    '4. Volver al Menú Principal',
    'Menu Transacciones',
    'Ir al Menú',h1, h2]

    opcion_menu_transacciones = request.form.get('opcion')

    return render_template('transacciones.html', **{'lista_menu': lista_menu})

@app.route('/cotizacion', methods=['GET', 'POST'])
def cotizacion():
    lista_menu =  [
    '1. Ver Cotización del Dolar Blue', 
    '2. Ver Cotización de Dolar Oficial', 
    '3. Volver al Menú',
    'Cotización Dolar',
    'Cotización',h1, h2]

    opcion_menu_transacciones = request.form.get('opcion')

    return render_template('transacciones.html', **{'lista_menu': lista_menu})
#Terminan Menus Principales#






if __name__ == '__main__':
    app.run()