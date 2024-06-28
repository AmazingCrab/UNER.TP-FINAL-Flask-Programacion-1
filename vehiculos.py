from flask import Flask, render_template, request

def vehiculos():
    lista_menu = [
    '1. Crear Vehículos', 
    '2. Editar Vehículos', 
    '3. Eliminar Vehículo', 
    '4. Listar Vehículo', 
    '5. Buscar Vehículo',
    '6. Volver al Menú Principal',
    'Menu Vehiculos',
    'Ir al Menú',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2

    opcion_menu_vehiculos = request.form.get('opcion')

    return render_template('vehiculos.html', **{'lista_menu': lista_menu})