from flask import Flask, send_from_directory

app = Flask(__name__)

# Ruta principal para servir el archivo README.md del repositorio
@app.route('/')
def index():
    return send_from_directory('/app/awesome-threat-intelligence', 'README.md')

# Ruta para servir cualquier archivo del repositorio
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('/app/awesome-threat-intelligence', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
