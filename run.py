# Importa o objeto 'app' e 'db' do módulo 'app'
# O 'app' é a instância da aplicação Flask e 'db' é a instância do banco de dados SQLAlchemy
from app import app, db

# Importa as classes 'User' e 'Item' do módulo 'app.models'
# Essas classes representam os modelos de dados (ou tabelas) que serão usados no banco de dados
from app.models import User, Item

# Usa o contexto da aplicação para garantir que todas as operações dentro desse bloco
# são executadas dentro do contexto da aplicação Flask. Isso é necessário para interagir com o banco de dados.
with app.app_context():
    # Cria todas as tabelas definidas pelos modelos (User, Item) no banco de dados
    # Se as tabelas já existem, essa operação não faz nada
    db.create_all()

# Verifica se o script está sendo executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    # Executa a aplicação Flask no modo de depuração (debug)
    # O modo de depuração é útil durante o desenvolvimento porque reinicia o servidor automaticamente
    # sempre que há uma mudança no código e também fornece mensagens de erro detalhadas
    app.run(debug=True)
