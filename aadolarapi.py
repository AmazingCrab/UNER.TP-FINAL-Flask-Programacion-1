import requests

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