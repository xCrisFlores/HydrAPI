import json
from flask import Flask
from flask_sock import Sock
from app import create_app
from app.services.consumption_service import ConsumptionService
app = create_app()

sock = Sock(app)

#Endpoint Web Socket para transmision de datos en tiempo real (Aun bajo pruebas)
@sock.route('/ws')
def websocket(ws):
    try:
        while True: 
            data = ws.receive() 

            if data:
                try:
                    formatedData = json.loads(data) 
                    print(f"Datos recibidos: {formatedData}")

                    consumption = ConsumptionService.create_resource(formatedData)

                except json.JSONDecodeError as e:
                    ws.send(json.dumps({"error": f"Error en formato JSON: {str(e)}"}))  
                    print(f"Error en formato JSON: {e}")

            else:
                break 

    except Exception as e:
        ws.send(json.dumps({"error": f"Error inesperado: {str(e)}"}))
        print(f"Error: {e}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
