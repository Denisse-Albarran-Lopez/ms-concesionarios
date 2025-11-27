from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.service.concesionaria_service import ConcesionariaService
from app.database import get_db

router = APIRouter()
concesionaria_service = ConcesionariaService()

class ConcesionariaRequest(BaseModel):
    numAutorizado: str
    dependencia: str
    autorizado: str
    horario_atencion: str

@router.post("/crear")
def crear_concesionaria(request: ConcesionariaRequest, db: Session = Depends(get_db)):
    return concesionaria_service.crear_concesionaria(
        db, request.numAutorizado, request.dependencia, 
        request.autorizado, request.horario_atencion
    )

@router.get("/qr/{numAutorizado}")
def obtener_concesionaria_por_qr(numAutorizado: str, db: Session = Depends(get_db)):
    return concesionaria_service.obtener_concesionaria_por_qr(db, numAutorizado)

@router.get("/todas")
def obtener_todas_concesionarias(db: Session = Depends(get_db)):
    return concesionaria_service.obtener_todas_concesionarias(db)