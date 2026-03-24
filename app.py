from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='/public')

print("🚀 Servidor iniciado")

# 🔹 Ruta principal
@app.route("/")
def home():
    return app.send_static_file("index.html")

# 🔹 Obtener productos
@app.route("/productos", methods=["GET"])
def get_productos():
    return jsonify([])  # temporal para evitar errores

# 🔹 Agregar producto
@app.route("/productos", methods=["POST"])
def add_producto():
    return jsonify({"mensaje": "ok"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)