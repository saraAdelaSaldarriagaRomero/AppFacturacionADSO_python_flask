from sqlalchemy import Column, Integer, String
from models import session, Base

class Categoria():
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    categoria = Column(String(300), unique=True, nullable=False)


def __init__(self, categoria):
        self.categoria = categoria