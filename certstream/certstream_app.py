import certstream
import logging
import json

# Configura el nivel de logging
logging.basicConfig(level=logging.INFO)

def print_callback(message, context):
    # Convierte el mensaje en un formato legible
    logging.info("Mensaje recibido: {}".format(json.dumps(message, indent=2)))

# Conéctate a la API de Certstream con la URL correcta
certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io')
