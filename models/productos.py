from sqlalchemy import Column, Integer, String, Float,ForeignKey

class Productos():
    __tablename__='productos'
    id = Column(Integer,prymary_key=True)
    descripcion = Column(String(300),unique=True, nullable=False)
    valor_unitario= Column(Float(10,8))
    unidad_medida= Column(String(3),nullable=False)
    cantidad_stock= Column(Float(10,8))
    categoria = Column(Integer,ForeignKey('categorias.id'),nullable=False)