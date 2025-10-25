from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/saludo')
def llamar_servicio():
    nombre = request.args.get('nombre', 'Invitado')  # Valor por defecto si no se pasa el parámetro
    url_objetivo = f'http://otsugua-otsugua04-dev.apps.rm2.thpm.p1.openshiftapps.com/saludo?nombre={nombre}'  # Reemplaza con tu API real

    try:
        respuesta = requests.get(url_objetivo)
        datos = respuesta.json()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

