## Este proyecto fue realizado en consola y en flask al 95% esta es la versión en flask.

# Aplicación Flask - Concesionario La Ñata

Esta es una sencilla aplicación Flask para un concesionario de automóviles llamado "Concesionario La Ñata".
Incluye operaciones CRUD para vehículos, clientes y transacciones. 
También incluye una característica de cotización del dolar utilizando la API de Bluelytics(valido para Argentina).

## Instalación

1. Clona este repositorio:

<bash>
git clone https://github.com/tu-usuario/flask-concesionario-la-nata.git
cd flask-concesionario-la-nata

2.Crea un entorno virtual (opcional pero recomendado):

python3 -m venv venv
source venv/bin/activate

3.Instala los paquetes necesarios:

pip install flask pandas requests

4.Ejecuta la aplicación:

python app.py

Ahora deberías poder acceder a la aplicación en http://localhost:5000.

Uso:
La aplicación un menú simple donde puedes navegar por diferentes secciones como Vehículos, Clientes, Transacciones y Cotización del Dólar.

Vehículos: Permite agregar, editar, eliminar y ver la información del vehículo.
Clientes: Permite agregar, editar, eliminar y ver la información del cliente.
Transacciones: Permite crear nuevas transacciones y ver una lista de todas las transacciones.
Cotización del Dólar: Muestra los valores actuales promedio, de venta y de compra del dólar utilizando la API de Bluelytics.

Notas
La aplicación utiliza archivos JSON para almacenar la información de vehículos, clientes y transacciones.
La aplicación utiliza la API de Bluelytics para obtener los tipos de cambio actuales del dólar.
La aplicación es un ejemplo básico y no incluye autenticación de usuarios ni características avanzadas.


Este README es una guía básica de instalación y instrucciones de uso para esta aplicación Flask.


CRUD CONCESIONARIA by Andrea Romero, Emanuel Conte Nahuel , Nahuel Marcilli is marked with CC0 1.0 
