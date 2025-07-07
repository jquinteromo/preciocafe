import os
from flask import Flask, jsonify
from flask_cors import CORS
from scraper import obtener_precio_cafe

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API de precio del café."})

@app.route("/api/precio", methods=["GET"])
def get_precio():
    precio = obtener_precio_cafe()
    if precio:
        return jsonify({"precio": precio})
    else:
        return jsonify({"error": "No se encontró el precio"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
