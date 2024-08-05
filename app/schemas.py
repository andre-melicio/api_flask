# Importa a classe Schema, o módulo fields e o módulo validate da biblioteca marshmallow
from marshmallow import Schema, fields, validate

# Define uma classe chamada ItemSchema que herda da classe Schema
class ItemSchema(Schema):
    # Define um campo 'name' que é uma string e é obrigatório
    # O campo 'name' deve ter pelo menos 1 caractere
    name = fields.Str(required=True, validate=validate.Length(min=1))

    # Define um campo 'description' que é uma string e é obrigatório
    # O campo 'description' deve ter pelo menos 1 caractere
    description = fields.Str(required=True, validate=validate.Length(min=1))

# Cria uma instância da classe ItemSchema
item_schema = ItemSchema()
