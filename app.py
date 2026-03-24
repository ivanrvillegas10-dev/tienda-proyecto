from flask import Flask, request, jsonify, send_from_directory
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

print("🚀 Servidor iniciado")

# 🔥 IMPORTANTE: para que funcione CSS/JS
app = Flask(__name__, static_folder='public', static_url_path='')

# 🔹 Conexión a la base de datos
def get_connection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    except Exception as e:
        print("❌ Error de conexión:", e)
        return None

# 🔹 Página principal
@app.route("/")
def home():
    return send_from_directory("public", "index.html")

# 🔹 Obtener productos
@app.route("/productos", methods=["GET"])
def get_productos():
    conn = get_connection()

    if conn is None:
        return jsonify([])

    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, precio FROM productos")
        rows = cur.fetchall()

        productos = []
        for r in rows:
            productos.append({
                "id": r[0],
                "nombre": r[1],
                "precio": float(r[2])
            })

        cur.close()
        conn.close()

        return jsonify(productos)

    except Exception as e:
        print("❌ Error en GET:", e)
        return jsonify([])

# 🔹 Agregar producto
@app.route("/productos", methods=["POST"])
def add_producto():
    data = request.json

    conn = get_connection()

    if conn is None:
        return jsonify({"mensaje": "Modo prueba (sin BD)"})

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO productos(nombre, precio) VALUES(%s, %s)",
            (data["nombre"], data["precio"])
        )
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"mensaje": "Producto agregado"})

    except Exception as e:
        print("❌ Error en POST:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
