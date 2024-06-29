from flask import Flask, render_template, request, url_for
import requests

import json

app = Flask(__name__, template_folder="templates",static_folder='../static')
app.config['FLASK_SKIP_CSRF'] = True
app.static_folder = 'static'

# Abrir y cargar el archivo clientes.json
with open('clientes.json', 'r') as clientes_file:
    clientes = json.load(clientes_file)

# Abrir y cargar el archivo ventas.json
with open('vehiculos.json', 'r') as vehiculos_file:
    vehiculos = json.load(vehiculos_file)
################################################################################
################################################################################
##############
##########      #      ######    #####  ####  ########
######        ####     #####    ####   ###########
###         ########    ##########    #######  #######

def asignarProximoId():
    if not dicccionario_json:
        return 1
        ultimoId = max(registro['id'] for registro in dicccionario_json)
    return ultimoId + 1





################################################################################
################################################################################
##############
##########      #      ######    #####  ####  ########
######        ####     #####    ####   ###########
###         ########    ##########    #######  #######
@app.route('/', methods=['GET', 'POST'])
def index():   
    lista_menu = [
        '1. Vehículos',
        '2. Clientes', 
        '3. Transacciones', 
        '4. Ver Cotización del Dolar',
        'Menú Principal',
        'Ir al Menú',
        'Concesionario La Ñata',
        'Bienvenido!'
    ]
    
    return render_template('index.html', lista_menu=lista_menu)


###############################################################
@app.route('/vehiculos', methods=['GET', 'POST'])
def vehiculos():
    lista_vehiculos = [
    '1. Crear Vehículos', 
    '2. Editar Vehículos', 
    '3. Eliminar Vehículo', 
    '4. Listar Vehículo', 
    '5. Buscar Vehículo',
    '6. Volver al Menú Principal',
    'Vehículos',
    'Ir al Menú',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2

    #opcion_menu_vehiculos = request.form.get('opcion')

    return render_template('vehiculos.html', **{'lista_vehiculos':lista_vehiculos})

@app.route('/vehiculos-crear', methods=['GET', 'POST'])
def vehiculos_crear():
    lista_crear = [
        'Concesionario La Ñata',  # h1
        'Bienvenido!',  # h2
        'Vehículo Nuevo'  # h3
    ]
    return render_template('vehiculos-crear.html', lista_crear=lista_crear)


@app.route("/submit-c-v", methods=["POST"])
def submit_form():
    form_data = request.form
    vehiculo_id = asignarProximoIdent(form_data)
    nuevo_vehiculo = {"patente": "s", "marca": "s", "modelo": "s", "tipo": "s", "anio": "s", "precio_compra": "s", "precio_venta": "s", "estado": "s", "submit": "Crear Veh\u00edculo"}

    
    print ((form_data))
    
    
    # Process the form data as needed
    # For example, save it to a database or perform some calculations
    with open('vehiculos.json', 'a') as file:
        json.dump(form_data, file)
        file.write('\n')


    return 'Form data received!'















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
    'Ir al Menú',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2


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
    'Ir al Menú',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2


    opcion_menu_transacciones = request.form.get('opcion')

    return render_template('transacciones.html', **{'lista_menu': lista_menu})

#################### DOLAR OKEY ####################
@app.route('/cotizacion', methods=['GET', 'POST'])
def cotizacion_ppal():
    blue_string, oficial_string = obtener_cotizacion_dolar()

    lista_menu =  [
    'Cotizacion del Dolar',
    'Dolar Blue',
    'Dolar Oficial',
    'Volver al Menu Principal',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2 

    headers = ['Dolar Promedio','Dolar Venta','Dolar Compra']
    fields1 = [blue_string]  # Dólar Blue
    fields2 = [oficial_string]  # Dólar Oficial
        
    return render_template('cotizacion.html', **{'lista_menu': lista_menu, 'headers': headers, 'fields1':fields1, 'fields2':fields2})

        #Integrar la plantilla cotizacion.html proporcionada
def obtener_cotizacion_dolar():
    url = 'https://api.bluelytics.com.ar/v2/latest'
    response = requests.get(url)
    
    if response.status_code == 200:
        dolar = response.json()
        blue = dolar['blue']
        oficial = dolar['oficial']
        
        blue_string = [str(blue.get('value_avg')), str(blue.get('value_sell')), str(blue.get('value_buy'))]
        oficial_string = [str(oficial.get('value_avg')), str(oficial.get('value_sell')), str(oficial.get('value_buy'))]
        
        return blue_string, oficial_string
    else:
        return [], []
####################################################