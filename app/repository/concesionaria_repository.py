from sqlalchemy.orm import Session
from app.models.models import Concesionaria

class ConcesionariaRepository:
    
    def crear_concesionaria(self, db: Session, numAutorizado: str, dependencia: str, autorizado: str, horario_atencion: str):
        db_concesionaria = Concesionaria(
            numAutorizado=numAutorizado,
            dependencia=dependencia,
            autorizado=autorizado,
            horario_atencion=horario_atencion
        )
        db.add(db_concesionaria)
        db.commit()
        db.refresh(db_concesionaria)
        return db_concesionaria
    
    def obtener_concesionaria_por_id(self, db: Session, id_concesionaria: int):
        return db.query(Concesionaria).filter(Concesionaria.id_concesionaria == id_concesionaria).first()
    
    def obtener_todas_concesionarias(self, db: Session):
        return db.query(Concesionaria).all()
    
    def obtener_concesionaria_por_qr(self, db: Session, numAutorizado: str):
        return db.query(Concesionaria).filter(Concesionaria.numAutorizado == numAutorizado).first()