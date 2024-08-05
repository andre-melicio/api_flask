from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
from PyPDF2 import PdfReader

# Cria uma instância da aplicação Flask, usando o nome do módulo atual.
app = Flask(__name__)

# Configuração do banco de dados usando PostgreSQL.
# Substitua <username>, <password>, <host>, <port>, <database> com suas informações do PostgreSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:coffee@localhost/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa rastreamento de modificações para melhorar a performance.

# Inicializa o SQLAlchemy com a aplicação Flask.
db = SQLAlchemy(app)

# Define o modelo de dados para o banco de dados.
# Um modelo é uma representação de uma tabela no banco de dados.
# Cada atributo da classe representa uma coluna da tabela.
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária.
    name = db.Column(db.String(50), nullable=False)  # Coluna 'name', tipo String, não pode ser nulo.
    description = db.Column(db.String(200), nullable=False)  # Coluna 'description', tipo String, não pode ser nulo.

# Cria todas as tabelas no banco de dados que ainda não existem.
db.create_all()

# Configuração da pasta de upload de arquivos.
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria a pasta se ela não existir.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configura o Flask para usar essa pasta para uploads.

# Define a rota principal da aplicação.
@app.route('/')
def index():
    return 'API está funcionando!'  # Retorna uma mensagem simples para confirmar que a API está funcionando.

# Define a rota para upload de arquivos.
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:  # Verifica se nenhum arquivo foi enviado.
        return jsonify({'error': 'Nenhum arquivo foi enviado'}), 400

    file = request.files['file']
    if file.filename == '':  # Verifica se o nome do arquivo está vazio.
        return jsonify({'error': 'Nome do arquivo vazio'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)  # Define o caminho completo do arquivo.
    file.save(filepath)  # Salva o arquivo na pasta de upload.

    # Processa arquivos CSV.
    if file.filename.endswith('.csv'):
        data = pd.read_csv(filepath)  # Lê o arquivo CSV.
        return jsonify({'message': 'CSV processado com sucesso', 'data': data.to_dict()}), 200

    # Processa arquivos PDF.
    elif file.filename.endswith('.pdf'):
        reader = PdfReader(filepath)
        text = ''
        for page in reader.pages:  # Extrai texto de cada página do PDF.
            text += page.extract_text()
        return jsonify({'message': 'PDF processado com sucesso', 'data': text}), 200

    # Retorna mensagem padrão se o tipo de arquivo não for suportado.
    return jsonify({'message': 'Arquivo enviado, mas o tipo não é suportado para o processamento.'}), 200

# CRUD: Lista todos os itens.
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Consulta todos os itens no banco de dados.
    items_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]  # Converte os itens para uma lista de dicionários.
    return jsonify(items_list), 200

# CRUD: Cria um novo item.
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()  # Obtém os dados JSON enviados na requisição.
    new_item = Item(name=data['name'], description=data['description'])  # Cria uma nova instância do modelo Item.
    db.session.add(new_item)  # Adiciona o novo item à sessão do banco de dados.
    db.session.commit()  # Salva (commita) a transação no banco de dados.
    return jsonify({'message': 'Item criado com sucesso!'}), 201

# CRUD: Lista um item específico.
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)  # Consulta o item pelo ID ou retorna um 404 se não for encontrado.
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description}), 200

# CRUD: Atualiza um item específico.
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()  # Obtém os dados JSON enviados na requisição.
    item = Item.query.get_or_404(item_id)  # Consulta o item pelo ID ou retorna um 404 se não for encontrado.
    item.name = data.get('name', item.name)  # Atualiza o nome do item se fornecido, caso contrário mantém o valor atual.
    item.description = data.get('description', item.description)  # Atualiza a descrição do item se fornecida, caso contrário mantém o valor atual.
    db.session.commit()  # Salva (commita) a transação no banco de dados.
    return jsonify({'message': 'Item atualizado com sucesso!'}), 200

# CRUD: Deleta um item específico.
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)  # Consulta o item pelo ID ou retorna um 404 se não for encontrado.
    db.session.delete(item)  # Remove o item da sessão do banco de dados.
    db.session.commit()  # Salva (commita) a transação no banco de dados.
    return jsonify({"message": "Item deletado com sucesso"}), 200

# Executa a aplicação Flask no modo de depuração.
if __name__ == '__main__':
    app.run(debug=True)
