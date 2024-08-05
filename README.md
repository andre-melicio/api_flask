# 📚 API de Estudos

Bem-vindo! Esta API é um exemplo didático que demonstra como criar uma aplicação web utilizando Flask, com integração a um banco de dados, autenticação JWT, limitação de requisições, e upload e processamento de arquivos.

## 🛠️ Tecnologias Utilizadas

- **Flask**: Micro framework web para Python.
- **Flask-SQLAlchemy**: Integração com SQLAlchemy para ORM.
- **Flask-JWT-Extended**: Autenticação e autorização com JWT.
- **Flask-Limiter**: Limitação de taxa de requisições.
- **psycopg2-binary**: Adaptador para PostgreSQL.
- **pandas**: Manipulação e análise de dados.
- **PyPDF2**: Manipulação de arquivos PDF.
- **marshmallow**: Serialização e validação de dados.
- **python-dotenv**: Carregamento de variáveis de ambiente.

## 📁 Estrutura do Projeto

```plaintext
api-de-estudos/
│
├── app/
│   ├── __init__.py  # Inicialização da aplicação Flask e suas extensões
│   ├── models.py    # Definição dos modelos de dados
│   ├── routes.py    # Definição das rotas da API
│   ├── schemas.py   # Definição dos esquemas de validação
│
├── migrations/      # Arquivos de migração do banco de dados
│
├── .env             # Arquivo de variáveis de ambiente
├── run.py           # Arquivo principal para rodar a aplicação
├── README.md        # Documentação do projeto
│
└── requirements.txt # Dependências do projeto
```

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.7+
- PostgreSQL

### Passo a Passo

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/api-de-estudos.git
   cd api-de-estudos
   ```

2. **Crie um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**

   - Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
     ```plaintext
     DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
     JWT_SECRET_KEY=sua_chave_secreta
     UPLOAD_FOLDER=uploads
     ```

5. **Crie as tabelas no banco de dados**

   ```bash
   flask db upgrade
   ```

6. **Inicie a aplicação**
   ```bash
   flask run
   ```

## 🌟 Funcionalidades

### Autenticação

- **Registro de Usuário**

  - Rota: `/register`
  - Método: `POST`
  - Payload:
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```

- **Login de Usuário**
  - Rota: `/login`
  - Método: `POST`
  - Payload:
    ```json
    {
      "username": "seu_usuario",
      "password": "sua_senha"
    }
    ```

### Itens

- **Obter Todos os Itens**

  - Rota: `/items`
  - Método: `GET`
  - Autenticação: JWT

- **Criar um Novo Item**

  - Rota: `/items`
  - Método: `POST`
  - Autenticação: JWT
  - Payload:
    ```json
    {
      "name": "nome_do_item",
      "description": "descrição_do_item"
    }
    ```

- **Obter um Item pelo ID**

  - Rota: `/items/<int:item_id>`
  - Método: `GET`
  - Autenticação: JWT

- **Atualizar um Item pelo ID**

  - Rota: `/items/<int:item_id>`
  - Método: `PUT`
  - Autenticação: JWT
  - Payload:
    ```json
    {
      "name": "novo_nome_do_item",
      "description": "nova_descrição_do_item"
    }
    ```

- **Deletar um Item pelo ID**
  - Rota: `/items/<int:item_id>`
  - Método: `DELETE`
  - Autenticação: JWT

### Upload de Arquivos

- **Upload de Arquivo**
  - Rota: `/upload`
  - Método: `POST`
  - Autenticação: JWT
  - Form-data:
    - `file`: Arquivo para upload (CSV ou PDF)

## 📑 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📞 Contato

Para mais informações, entre em contato com [andre.melicio@outlook.com](mailto:andre.melicio@outlook.com).

---

Espero que você aproveite e aprenda com esta API! 🚀📚
