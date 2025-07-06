from flask import Flask, jsonify
from scraper import obtener_precio_cafe

app = Flask(__name__)

@app.route("/api/precio", methods=["GET"])
def get_precio():
    precio = obtener_precio_cafe()
    if precio:
        return jsonify({"precio": precio})
    else:
        return jsonify({"error": "No se encontró el precio"}), 500

if __name__ == "__main__":
    app.run(debug=True)
