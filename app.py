from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/saludo/<nombre>')
def llamar_servicio(nombre):
    url_objetivo = f'http://otsugua-otsugua04-dev.apps.rm2.thpm.p1.openshiftapps.com/saludo?nombre={nombre}'  # Reemplaza con tu API real
    try:
        respuesta = requests.get(url_objetivo)
        datos = respuesta.json()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)