from flask import Flask, request
from datetime import datetime
import csv
import os

app = Flask(__name__)

ARQUIVO = "localizacoes.csv"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["data_hora", "latitude", "longitude", "ip"])

@app.route("/api", methods=["POST"])
def salvar_localizacao():
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    ip = request.remote_addr
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([agora, latitude, longitude, ip])

    print(f"[{agora}] Localização salva: {latitude}, {longitude} | IP: {ip}")
    return "OK", 200

@app.route("/")
def status():
    return "Servidor online. Use /api para enviar dados de localização."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
