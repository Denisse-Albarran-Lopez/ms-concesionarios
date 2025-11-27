from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from typing import Optional, List

app = FastAPI(title="MS-Concesionarios", description="Microservicio de concesionarios")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta del archivo de concesionarios
CONCESIONARIOS_FILE = r"C:\Users\Denisse Albarrán Lpz\OneDrive\Escritorio\Ingeniería de Software\Pruebas\MS-Concesionarios\concesionario_001.txt"

# Modelos Pydantic
class Concesionario(BaseModel):
    Id_concesionaria: int
    numAutorizado: str
    dependencia: str
    autorizado: str
    horario_atencion: str

class ConcesionarioCreate(BaseModel):
    numAutorizado: str
    dependencia: str
    autorizado: str
    horario_atencion: str

# Funciones auxiliares
def load_concesionarios():
    if not os.path.exists(CONCESIONARIOS_FILE):
        return []
    
    concesionarios = []
    try:
        with open(CONCESIONARIOS_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            
            # Parsear formato clave: valor
            lines = content.split('\n')
            concesionario = {}
            
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    concesionario[key.strip()] = value.strip()
            
            if concesionario:
                concesionarios.append(concesionario)
                
    except Exception as e:
        print(f"Error loading concesionarios: {e}")
        return []
    
    return concesionarios

def save_concesionario(concesionario_data):
    with open(CONCESIONARIOS_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Id_concesionaria: {concesionario_data['Id_concesionaria']}\n")
        f.write(f"numAutorizado: {concesionario_data['numAutorizado']}\n")
        f.write(f"dependencia: {concesionario_data['dependencia']}\n")
        f.write(f"autorizado: {concesionario_data['autorizado']}\n")
        f.write(f"horario_atencion: {concesionario_data['horario_atencion']}")

def find_concesionario_by_num(num_autorizado: str):
    concesionarios = load_concesionarios()
    return next((c for c in concesionarios if c.get('numAutorizado') == num_autorizado), None)

# Endpoints
@app.get("/")
async def root():
    return {"mensaje": "MS-Concesionarios - Microservicio de concesionarios"}

@app.get("/concesionarias/qr/{numAutorizado}")
async def obtener_por_qr(numAutorizado: str):
    concesionario = find_concesionario_by_num(numAutorizado)
    if not concesionario:
        raise HTTPException(status_code=404, detail="Concesionario no encontrado")
    
    return {
        "Id_concesionaria": int(concesionario.get('Id_concesionaria', 0)),
        "numAutorizado": concesionario.get('numAutorizado'),
        "dependencia": concesionario.get('dependencia'),
        "autorizado": concesionario.get('autorizado'),
        "horario_atencion": concesionario.get('horario_atencion')
    }

@app.post("/concesionarias/crear")
async def crear_concesionario(concesionario: ConcesionarioCreate):
    # Verificar si ya existe
    if find_concesionario_by_num(concesionario.numAutorizado):
        raise HTTPException(status_code=400, detail="El concesionario ya existe")
    
    # Obtener nuevo ID
    concesionarios = load_concesionarios()
    nuevo_id = len(concesionarios) + 1
    
    concesionario_data = {
        "Id_concesionaria": nuevo_id,
        "numAutorizado": concesionario.numAutorizado,
        "dependencia": concesionario.dependencia,
        "autorizado": concesionario.autorizado,
        "horario_atencion": concesionario.horario_atencion
    }
    
    save_concesionario(concesionario_data)
    
    return {
        "mensaje": "Concesionario creado exitosamente",
        "concesionario": concesionario_data
    }

@app.get("/concesionarias/todas")
async def obtener_todas():
    concesionarios = load_concesionarios()
    return {"concesionarios": concesionarios}

@app.put("/concesionarias/{numAutorizado}")
async def actualizar_concesionario(numAutorizado: str, concesionario: ConcesionarioCreate):
    concesionario_existente = find_concesionario_by_num(numAutorizado)
    if not concesionario_existente:
        raise HTTPException(status_code=404, detail="Concesionario no encontrado")
    
    concesionario_data = {
        "Id_concesionaria": int(concesionario_existente.get('Id_concesionaria', 1)),
        "numAutorizado": concesionario.numAutorizado,
        "dependencia": concesionario.dependencia,
        "autorizado": concesionario.autorizado,
        "horario_atencion": concesionario.horario_atencion
    }
    
    save_concesionario(concesionario_data)
    
    return {
        "mensaje": "Concesionario actualizado exitosamente",
        "concesionario": concesionario_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)