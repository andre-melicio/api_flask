# Importa os módulos e funções necessários
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Configurações da aplicação
# Configura a URI do banco de dados, obtida da variável de ambiente DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Desativa o rastreamento de modificações do SQLAlchemy para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configura a chave secreta para JWT, obtida da variável de ambiente JWT_SECRET_KEY
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# Configura a pasta de upload, obtida da variável de ambiente UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

# Cria uma instância do banco de dados SQLAlchemy
db = SQLAlchemy(app)
# Cria uma instância do gerenciador de JWT
jwt = JWTManager(app)
# Cria uma instância do Limiter para limitar a taxa de requisições
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

# Configura a pasta de upload localmente e garante que ela exista
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Importa as rotas da aplicação
from app import routes
