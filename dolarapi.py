from flask import Flask, render_template, request


url = 'https://api.bluelytics.com.ar/v2/latest'
response = requests.get(url)
#class dolar: falta definir la api como objeto
if response.status_code == 200:
    # Obtén los datos JSON de la respuesta
        dolar = response.json()
        #data['oficial']
        #data['blue']

blue_string = []
for elemento in dolar['blue']:
    blue_string.append(str(dolar['blue'].get(elemento)))

oficial_string = []
for elemento in dolar['oficial']:
    oficial_string.append(str(dolar['oficial'].get(elemento)))