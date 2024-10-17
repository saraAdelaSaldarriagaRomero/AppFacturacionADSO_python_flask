from sqlalchemy import Column, Integer, String, Float,Date

class Clientes():
    __tablename__='clientes'
    id = Column(Integer,prymary_key=True)
    nombre_completo = Column(String(300),unique=False, nullable=False)
    direccion = Column(String(300),unique=False, nullable=False)
    fecha_nacimiento = Column(Date(20),unique=False, nullable=False)
    telefono = Column(Integer,(20),unique=False, nullable=False)