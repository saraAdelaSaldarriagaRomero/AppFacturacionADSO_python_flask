from sqlalchemy import Column, Integer, String


class Categoria():
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    categoria = Column(String(300), unique=True, nullable=False)
