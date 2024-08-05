# Importa o objeto 'db' do módulo 'app'
from app import db

# Define a classe User que representa a tabela de usuários no banco de dados
class User(db.Model):
    # Define a coluna 'id' como chave primária e de tipo Integer
    id = db.Column(db.Integer, primary_key=True)

    # Define a coluna 'username' como String de tamanho 50, deve ser única e não pode ser nula
    username = db.Column(db.String(50), unique=True, nullable=False)

    # Define a coluna 'password_hash' como String de tamanho 200, não pode ser nula
    password_hash = db.Column(db.String(200), nullable=False)

# Define a classe Item que representa a tabela de itens no banco de dados
class Item(db.Model):
    # Define a coluna 'id' como chave primária e de tipo Integer
    id = db.Column(db.Integer, primary_key=True)

    # Define a coluna 'name' como String de tamanho 50, não pode ser nula
    name = db.Column(db.String(50), nullable=False)

    # Define a coluna 'description' como String de tamanho 200, não pode ser nula
    description = db.Column(db.String(200), nullable=False)

    # Define uma nova coluna 'new_column' como String de tamanho 100, pode ser nula
    new_column = db.Column(db.String(100), nullable=True)
