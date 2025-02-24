from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS  # Jika diperlukan untuk akses dari perangkat luar

# Koneksi ke MongoDB Atlas
uri = "mongodb+srv://timtujuh:vV2WEXiqjSTmPevl@clustertimtujuh.8p34h.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTimTujuh"

app = Flask(__name__)
CORS(app)  # Mengizinkan akses dari perangkat luar (opsional)

# Inisialisasi MongoDB
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database("TimTujuhDatabase")  # Ganti sesuai nama database Anda
my_collections = db.get_collection("MySensorData")  # Ganti sesuai nama koleksi Anda

@app.route("/sensor", methods=["POST"])
def receive_data():
    try:
        data = request.json
        print("[DEBUG] Data diterima dari ESP32:", data)

        # Validasi format data
        required_keys = {"humidity", "temperature", "motion", "ldr",}
        if not all(key in data and isinstance(data[key], (int, float)) for key in required_keys):
            return jsonify({"error": "Format data tidak valid!"}), 400

        # Simpan ke MongoDB
        my_collections.insert_one(data)

        return jsonify({"message": "Data berhasil disimpan"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)