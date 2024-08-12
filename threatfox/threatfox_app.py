import requests
import logging
import time

# Configurar el logging
logging.basicConfig(level=logging.INFO)

def fetch_threat_data():
    url = "https://threatfox-api.abuse.ch/api/v1/"
    data = {
        "query": "get_iocs",
        "days": 1
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        logging.info("Datos recibidos: %s", response.json())
    else:
        logging.error("Error al recibir datos: %s", response.status_code)

if __name__ == "__main__":
    fetch_threat_data()
    while True:
        time.sleep(3600)  # Mantiene el contenedor corriendo, durmiendo por una hora en cada iteración
