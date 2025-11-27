from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Concesionaria(Base):
    __tablename__ = "concesionaria"
    
    id_concesionaria = Column(Integer, primary_key=True, index=True)
    numAutorizado = Column(String, nullable=False)
    dependencia = Column(String, nullable=False)
    autorizado = Column(String, nullable=False)
    horario_atencion = Column(String, nullable=False)