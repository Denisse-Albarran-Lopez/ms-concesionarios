import requests
import json

BASE_URL = "http://localhost:8001"

def test_obtener_por_qr():
    # Probar con el número que está en el archivo
    response = requests.get(f"{BASE_URL}/concesionarias/qr/1062")
    print("Obtener por QR (1062):", response.json())

def test_obtener_todas():
    response = requests.get(f"{BASE_URL}/concesionarias/todas")
    print("Obtener todas:", response.json())

def test_crear_concesionario():
    data = {
        "numAutorizado": "1063",
        "dependencia": "Facultad de Ciencias",
        "autorizado": "Nuevo Concesionario S.A.",
        "horario_atencion": "Lunes a viernes de 7:00 a 19:00 horas"
    }
    response = requests.post(f"{BASE_URL}/concesionarias/crear", json=data)
    print("Crear concesionario:", response.json())

if __name__ == "__main__":
    print("Probando endpoints del MS-Concesionarios...")
    print("Asegúrate de que el servidor esté ejecutándose en localhost:8001")
    print()
    
    try:
        test_obtener_por_qr()
        test_obtener_todas()
        test_crear_concesionario()
    except requests.exceptions.ConnectionError:
        print("Error: No se puede conectar al servidor. Asegúrate de que esté ejecutándose.")
    except Exception as e:
        print(f"Error: {e}")