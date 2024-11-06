from sqlalchemy import Column, Integer, String, Date
from models import session, Base


class Clientes(Base):
    __tablename__='clientes'
    id = Column(Integer,primary_key=True)
    nombre_completo = Column(String(300),unique=False, nullable=False)
    direccion = Column(String(300),unique=False, nullable=False)
    fecha_nacimiento = Column(Date,unique=False, nullable=False)
    telefono = Column(Integer,unique=False, nullable=False)


    def __init__(self, nombre_completo, direccion, fecha_nacimiento, telefono):
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono