from flask import Flask, request, jsonify
from bot import iniciar_bot, asignar_rol
import asyncio

app = Flask(__name__)


loop = iniciar_bot()

# rcibir el json desde webhook (test4 , si no volvemos a POST)
@app.route('/webhook-compra', methods=['POST'])
def webhook_compra():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No se recibiO JSON validp'}), 400
    discord_id = data.get('discord_id')
    compra_verificada = data.get('compra_verificada', False)
    
    
    #manejop de errores
    
    if not discord_id:
        return jsonify({'error': 'Falta el discord_id o no anda tu host '}), 400

    if not compra_verificada:
        return jsonify({'error': 'compra_verificada debe ser true'}), 400

    try:
        future = asyncio.run_coroutine_threadsafe(asignar_rol(int(discord_id)), loop)
        future.result(timeout=10)
        return jsonify({'status': 'rol asignado'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al asignar rol (revisa el rol)(ya era cliente, ignorar el mensaje): {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=8080)
