# Importa módulos e funções necessárias do Flask e outras bibliotecas
from flask import request, jsonify
from app import app, db
from app.models import User, Item
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields, validate, ValidationError
import os
import pandas as pd
from PyPDF2 import PdfReader

# Define um esquema de validação usando marshmallow para os itens
class ItemSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=True, validate=validate.Length(min=1))

# Cria uma instância do esquema de item
item_schema = ItemSchema()

# Rota para registrar um novo usuário
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Obtém os dados do corpo da requisição
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():  # Verifica se o usuário já existe
        return jsonify({"msg": "Usuário já existe"}), 409
    password_hash = generate_password_hash(password)  # Gera um hash da senha
    new_user = User(username=username, password_hash=password_hash)  # Cria uma nova instância de usuário
    db.session.add(new_user)  # Adiciona o novo usuário ao banco de dados
    db.session.commit()  # Confirma a transação
    return jsonify({"msg": "Usuário registrado com sucesso"}), 201

# Rota para login de um usuário
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Obtém os dados do corpo da requisição
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()  # Busca o usuário no banco de dados
    if not user or not check_password_hash(user.password_hash, password):  # Verifica as credenciais
        return jsonify({"msg": "Credenciais inválidas"}), 401
    access_token = create_access_token(identity=username)  # Cria um token de acesso JWT
    return jsonify(access_token=access_token), 200

# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
@jwt_required()  # Requer autenticação JWT
def get_items():
    items = Item.query.all()  # Busca todos os itens no banco de dados
    items_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(items_list), 200

# Rota para criar um novo item
@app.route('/items', methods=['POST'])
@jwt_required()  # Requer autenticação JWT
def create_item():
    try:
        data = item_schema.load(request.get_json())  # Valida e desserializa os dados recebidos
    except ValidationError as err:
        return jsonify(err.messages), 400  # Retorna erros de validação, se houver
    new_item = Item(name=data['name'], description=data['description'])  # Cria uma nova instância de item
    db.session.add(new_item)  # Adiciona o novo item ao banco de dados
    db.session.commit()  # Confirma a transação
    return jsonify({'message': 'Item criado com sucesso!'}), 201

# Rota para obter um item específico pelo ID
@app.route('/items/<int:item_id>', methods=['GET'])
@jwt_required()  # Requer autenticação JWT
def get_item(item_id):
    item = Item.query.get_or_404(item_id)  # Busca o item pelo ID ou retorna 404 se não encontrado
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200

# Rota para atualizar um item específico pelo ID
@app.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()  # Requer autenticação JWT
def update_item(item_id):
    data = request.get_json()  # Obtém os dados do corpo da requisição
    item = Item.query.get_or_404(item_id)  # Busca o item pelo ID ou retorna 404 se não encontrado
    item.name = data.get('name', item.name)  # Atualiza o nome do item, se fornecido
    item.description = data.get('description', item.description)  # Atualiza a descrição do item, se fornecida
    db.session.commit()  # Confirma a transação
    return jsonify({'message': 'Item atualizado com sucesso!'}), 200

# Rota para deletar um item específico pelo ID
@app.route('/items/<int:id>', methods=['DELETE'])
@jwt_required()  # Requer autenticação JWT
def delete_item(id):
    item = Item.query.get_or_404(id)  # Busca o item pelo ID ou retorna 404 se não encontrado
    db.session.delete(item)  # Deleta o item do banco de dados
    db.session.commit()  # Confirma a transação
    return jsonify({"message": "Item deletado com sucesso"}), 200

# Rota para fazer upload de arquivos
@app.route('/upload', methods=['POST'])
@jwt_required()  # Requer autenticação JWT
def upload_file():
    if 'file' not in request.files:  # Verifica se um arquivo foi enviado
        return jsonify({'error': 'Nenhum arquivo foi enviado'}), 400

    file = request.files['file']
    if file.filename == '':  # Verifica se o nome do arquivo não está vazio
        return jsonify({'error': 'Nome do arquivo vazio'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)  # Define o caminho para salvar o arquivo
    file.save(filepath)  # Salva o arquivo no caminho especificado

    if file.filename.endswith('.csv'):  # Verifica se o arquivo é um CSV
        data = pd.read_csv(filepath)  # Lê o arquivo CSV usando pandas
        return jsonify({'message': 'CSV processado com sucesso', 'data': data.to_dict()}), 200

    elif file.filename.endswith('.pdf'):  # Verifica se o arquivo é um PDF
        reader = PdfReader(filepath)  # Lê o arquivo PDF usando PyPDF2
        text = ''
        for page in reader.pages:
            text += page.extract_text()  # Extrai o texto de cada página do PDF
        return jsonify({'message': 'PDF processado com sucesso', 'data': text}), 200

    return jsonify({'message': 'Arquivo enviado, mas o tipo não é suportado para o processamento.'}), 200
