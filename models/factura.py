from sqlalchemy import Column, Integer, ForeignKey,Date
from models import session, Base
class Facturas():
    __tablename__='facturas'
    id = Column(Integer,prymary_key=True)
    numero_factura = Column(Integer,(20),unique=True, nullable=False)
    fecha= Column(Date,(20),unique=False, nullable=False)

    
    
def __init__(self, numero_factura, fecha):
        self.numero_factura = numero_factura
        self.fecha = fecha