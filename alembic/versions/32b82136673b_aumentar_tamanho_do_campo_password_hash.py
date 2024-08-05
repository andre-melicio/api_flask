"""
Aumentar tamanho do campo password_hash

Revision ID: 32b82136673b
Revises: 191ce81600f1
Create Date: 2024-08-04 10:56:16.227667
"""

# Importa os módulos necessários
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Identificadores de revisão usados pelo Alembic
revision = '32b82136673b'  # ID da revisão atual
down_revision = '191ce81600f1'  # ID da revisão anterior
branch_labels = None
depends_on = None

# Função de upgrade para aplicar as alterações no banco de dados
def upgrade():
    # Altera a coluna 'password_hash' na tabela 'user'
    op.alter_column('user', 'password_hash',
               existing_type=sa.String(length=100),  # Tipo de dado existente (String de comprimento 100)
               type_=sa.String(length=200),  # Novo tipo de dado (String de comprimento 200)
               existing_nullable=False)  # A coluna não permite valores nulos

# Função de downgrade para reverter as alterações no banco de dados
def downgrade():
    # Altera a coluna 'password_hash' na tabela 'user' para seu estado original
    op.alter_column('user', 'password_hash',
               existing_type=sa.String(length=200),  # Tipo de dado existente (String de comprimento 200)
               type_=sa.String(length=100),  # Novo tipo de dado (String de comprimento 100)
               existing_nullable=False)  # A coluna não permite valores nulos
