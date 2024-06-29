from flask import Flask, render_template, redirect, url_for

import requests
import json

from vehiculos import *
from clientes import *
from transacciones import *
#from dolarapi import *

# Abrir y cargar el archivo clientes.json
with open('clientes.json', 'r') as clientes_file:
    clientes = json.load(clientes_file)

# Abrir y cargar el archivo ventas.json
with open('vehiculos.json', 'r') as vehiculos_file:
    vehiculos = json.load(vehiculos_file)



app = Flask(__name__, template_folder="templates",static_folder='../static')
app.config['FLASK_SKIP_CSRF'] = True
app.static_folder = 'static'

global lista_menu

# Variables globales

# Función para obtener la cotización del dólar


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
def vehiculos_ppal():
    # def vehiculos():
     lista_menu = [
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
 
     opcion_menu_vehiculos = request.form.get('opcion')
 
     return render_template('vehiculos.html', **{'lista_menu': lista_menu})
   # return vehiculos()

@app.route('/vehiculos-crear', methods=['GET', 'POST'])
#def vehiculos_crear():
#    return vehiculosCrear()

#@app.route('/vehiculos-crear', methods=['POST'])

#def update_json(file_path, new_dictionary):
#    update_json('vehiculos.json', auto_nuevo)
#    with open(file_path, 'r+') as f:
#        data = json.load(f)
#        data.update(new_dictionary)
#        f.seek(0)
#        json.dump(data, f, indent=4)


def guardar_auto_nuevo():
    formulario = request.form
    auto_nuevo = dict(formulario)
    
#    update_json('vehiculos.json', auto_nuevo)
    with open(vehiculos.json, 'r+') as f:
        data = json.load(f)

    with load(vehiculos.json, 'r+') as f:
        data = json.load(f)
        data.update(auto_nuevo)
        f.seek(0)
        json.dump(data, f, indent=4)

 #   update_json('vehiculos.json', auto_nuevo)

    return 'Datos del formulario guardados en el diccionario.'




#################################################################

@app.route('/clientes', methods=['GET', 'POST'])
def clientes_ppal():
    return clientes()


@app.route('/transacciones', methods=['GET', 'POST'])
def transacciones_ppal():
    return transacciones()




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