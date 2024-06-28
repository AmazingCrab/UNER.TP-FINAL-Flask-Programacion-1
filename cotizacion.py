from flask import Flask, render_template, request

dolar_actual = [['1000','800','1200']]

def cotizacion():
    lista_menu =  [
    'Cotizacion del Dolar',
    'Dolar Blue',
    'Dolar Oficial',
    'Volver al Menu Principal',
    'Concesionario La Ñata',#h1
    'Bienvenido!'] #h2

    headers = ['Dolar Promedio','Dolar Venta','Dolar Compra']

    return render_template('cotizacion.html', **{'lista_menu': lista_menu, 'headers': headers, 'fields1': dolar_actual, 'fields2':dolar_actual})