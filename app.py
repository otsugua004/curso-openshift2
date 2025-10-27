from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/saludo')
def llamar_servicio():
    nombre = request.args.get('nombre', 'Invitado')  # Valor por defecto si no se pasa el parámetro
    url_objetivo = f'http://otsugua-otsugua04-dev.apps.rm2.thpm.p1.openshiftapps.com/saludo?nombre={nombre}'  # Reemplaza con tu API real

    try:
        respuesta = requests.get(url_objetivo)
        return respuesta.text
    except Exception as e:
        return f"Error al llamar al servicio 1: {str(e)}", 500

@app.route('/startup', methods=['GET'])
def startup():
    return "Ok",200

@app.route('/readiness', methods=['GET'])
def readiness():
    return "Ok",200

@app.route('/health', methods=['GET'])
def health():
    return "Ok",200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

