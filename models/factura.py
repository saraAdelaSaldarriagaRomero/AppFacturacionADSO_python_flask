from sqlalchemy import Column, Integer, ForeignKey,Date

class Facturas():
    __tablename__='facturas'
    id = Column(Integer,prymary_key=True)
    numero_factura = Column(Integer,(20),unique=True, nullable=False)
    fecha= Column(Date,(20),unique=False, nullable=False)
    
