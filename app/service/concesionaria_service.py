from sqlalchemy.orm import Session
from app.repository.concesionaria_repository import ConcesionariaRepository
from fastapi import HTTPException

class ConcesionariaService:
    def __init__(self):
        self.concesionaria_repo = ConcesionariaRepository()
    
    def crear_concesionaria(self, db: Session, numAutorizado: str, dependencia: str, autorizado: str, horario_atencion: str):
        concesionaria_existente = self.concesionaria_repo.obtener_concesionaria_por_qr(db, numAutorizado)
        if concesionaria_existente:
            raise HTTPException(status_code=400, detail="El número autorizado ya existe")
        
        concesionaria = self.concesionaria_repo.crear_concesionaria(db, numAutorizado, dependencia, autorizado, horario_atencion)
        return {"mensaje": "Concesionaria creada exitosamente", "concesionaria_id": concesionaria.id_concesionaria}
    
    def obtener_concesionaria_por_qr(self, db: Session, numAutorizado: str):
        concesionaria = self.concesionaria_repo.obtener_concesionaria_por_qr(db, numAutorizado)
        if not concesionaria:
            raise HTTPException(status_code=404, detail="Concesionaria no encontrada")
        
        return {
            "id_concesionaria": concesionaria.id_concesionaria,
            "numAutorizado": concesionaria.numAutorizado,
            "dependencia": concesionaria.dependencia,
            "autorizado": concesionaria.autorizado,
            "horario_atencion": concesionaria.horario_atencion
        }
    
    def obtener_todas_concesionarias(self, db: Session):
        concesionarias = self.concesionaria_repo.obtener_todas_concesionarias(db)
        return [
            {
                "id_concesionaria": c.id_concesionaria,
                "numAutorizado": c.numAutorizado,
                "dependencia": c.dependencia,
                "autorizado": c.autorizado,
                "horario_atencion": c.horario_atencion
            }
            for c in concesionarias
        ]