from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# Lista de IPs permitidas
ips_permitidas = set()

@app.route('/')
def index():
    return "Servidor en ejecución. Usa el panel para gestionar las IPs."

@app.route('/permitir_conexion', methods=['GET'])
def permitir_conexion():
    ip = request.args.get('ip')
    if ip:
        ips_permitidas.add(ip)
        return jsonify({"success": True, "message": "Conexión permitida."})
    return jsonify({"success": False, "message": "IP no proporcionada."})

@app.route('/rechazar_conexion', methods=['GET'])
def rechazar_conexion():
    ip = request.args.get('ip')
    if ip:
        ips_permitidas.discard(ip)
        return jsonify({"success": True, "message": "Conexión rechazada."})
    return jsonify({"success": False, "message": "IP no proporcionada."})

@app.route('/generar_camara', methods=['GET'])
def generar_camara():
    # Verificar si la IP es permitida
    ip = request.remote_addr
    if ip in ips_permitidas:
        # Generar HTML temporal con acceso a la cámara
        camara_html = '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Acceso a la cámara</title>
        </head>
        <body>
            <h1>Acceso a la cámara en vivo</h1>
            <video id="video" width="320" height="240" autoplay></video>
            <script>
                if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                    navigator.mediaDevices.getUserMedia({ video: true })
                        .then(function(stream) {
                            var video = document.getElementById('video');
                            video.srcObject = stream;
                        }).catch(function(error) {
                            console.log("Error al acceder a la cámara: ", error);
                        });
                } else {
                    alert("Tu navegador no soporta el acceso a la cámara.");
                }
            </script>
        </body>
        </html>
        '''
        return render_template_string(camara_html)
    return jsonify({"success": False, "message": "Acceso denegado."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
