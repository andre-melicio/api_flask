# Flask é um micro framework web para Python. Ele permite a criação de aplicações web de forma rápida e simples.
from flask import Flask

# Flask-SQLAlchemy é uma extensão para Flask que adiciona suporte para SQLAlchemy.
# SQLAlchemy é uma biblioteca para mapeamento objeto-relacional (ORM) que facilita a interação com bancos de dados.
from flask_sqlalchemy import SQLAlchemy

# Flask-JWT-Extended é uma extensão para Flask que adiciona suporte para JSON Web Tokens (JWT).
# JWT é um padrão para criação de tokens de acesso que podem ser usados para autenticação e autorização.
from flask_jwt_extended import JWTManager

# Flask-Limiter é uma extensão para Flask que permite a limitação de taxa (rate limiting).
# Isso é útil para controlar o número de requisições que podem ser feitas a uma rota em um determinado período de tempo.
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# psycopg2-binary é um adaptador de banco de dados PostgreSQL para Python.
# Ele permite que aplicações Python se conectem e interajam com bancos de dados PostgreSQL.
import psycopg2-binary

# pandas é uma biblioteca poderosa para análise e manipulação de dados em Python.
# Ela fornece estruturas de dados flexíveis e expressivas como DataFrame, que facilita o trabalho com dados tabulares.
import pandas as pd

# PyPDF2 é uma biblioteca para trabalhar com arquivos PDF em Python.
# Ela permite ler, manipular e criar documentos PDF.
from PyPDF2 import PdfReader

# marshmallow é uma biblioteca para serialização e desserialização de objetos complexos em tipos de dados Python nativos.
# Isso é útil para converter dados de e para formatos como JSON.
from marshmallow import Schema, fields, validate, ValidationError

# python-dotenv é uma biblioteca que carrega variáveis de ambiente de um arquivo .env para o ambiente do sistema.
# Isso é útil para gerenciar configurações da aplicação de forma segura e prática.
from dotenv import load_dotenv
