# Importa a instância do SQLAlchemy do seu aplicativo
from app import db

# Define a metadata do banco de dados como a metadata da instância do SQLAlchemy
target_metadata = db.metadata
