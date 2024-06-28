from flask import Flask, render_template, request
from vehiculos import *
from clientes import *
from transacciones import *
from cotizacion import *


app = Flask(__name__, template_folder="templates")


global opcion_menu_ppal , opcion_menu_vechiculos ,opcion_menu_clientes, opcion_menu_ppal_transaccion 
global sub_op_menu_vehiculo, sub_op_menu_cliente, sub_op_menu_transacciones



@app.route('/', methods=['GET', 'POST'])
def index():# menu ppal
    lista_menu = [
    '1. Vehículos',
    '2. Clientes', 
    '3. Transacciones', 
    '4. Ver Cotización del Dolar',
    'Menú Principal',
    'Ir al Menú',#h3
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2
     
    opcion_menu_ppal = request.form.get('opcion')
    
    return render_template('index.html', **{'lista_menu': lista_menu})
@app.route('/vehiculos', methods=['GET', 'POST'])
def vehiculos_ppal():# menu vehiculos
    return vehiculos()
@app.route('/clientes', methods=['GET', 'POST'])
def clientes_ppal():# menu clientes
   return clientes()
@app.route('/transacciones', methods=['GET', 'POST'])
def transacciones_ppal():# menu transacciones
    return transacciones()
@app.route('/cotizacion', methods=['GET', 'POST'])
def cotizacion_ppal():# menu cotizacion
    return cotizacion()
#Terminan Menus Principales#






    




if __name__ == '__main__':
    app.run()