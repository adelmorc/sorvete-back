# 🍦 Sorveteria App - Backend (API RESTful)

Este é o repositório do backend do aplicativo "Sorveteria", construído com Django REST Framework. Ele fornece uma API RESTful para o frontend gerenciar produtos, usuários, estoque e outras funcionalidades.

## ✨ Funcionalidades da API

-   **Autenticação JWT:** Gerenciamento de usuários e autenticação via tokens JWT (utilizando `djangorestframework-simplejwt`).
-   **Gerenciamento de Produtos:** CRUD (Criar, Ler, Atualizar, Deletar) de produtos (sorvetes, sabores, preços).
-   **Gerenciamento de Estoque:** Controle de quantidade e movimentação de itens no estoque.
-   **Gerenciamento de Fornecedores:** CRUD de informações de fornecedores.
-   **Endpoints RESTful:** API bem definida e documentada.

## 🚀 Tecnologias Utilizadas

-   **Python 3.12.3**
-   **Django**
-   **Django REST Framework**
-   `djangorestframework-simplejwt` para autenticação
-   `psycopg2` (ou outro driver de banco de dados, dependendo do `DB_ENGINE` no `.env`)
-   `python-dotenv` para variáveis de ambiente

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

-   [Python 3.12.3](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)
-   [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) ou [venv](https://docs.python.org/3/library/venv.html) (para ambientes virtuais)
-   [PostgreSQL](https://www.postgresql.org/download/) (se você for usar PostgreSQL, caso contrário, SQLite já vem com Python)

## 💻 Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/seu_usuario/sorvete-back.git](https://github.com/seu_usuario/sorvete-back.git)
    cd sorvete-back # Ou cd sorvetes, dependendo da sua estrutura raiz
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv pe_venv # Substitua 'pe_venv' pelo nome do seu ambiente virtual, se for diferente
    source pe_venv/bin/activate # No Linux/macOS
    # pe_venv\Scripts\activate # No Windows
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto (ao lado do `manage.py`, ou em `core/.env` se for o caso) com as seguintes variáveis:
    ```
    SECRET_KEY=sua_secret_key_super_secreta
    DEBUG=True
    DB_ENGINE=django.db.backends.sqlite3 # ou django.db.backends.postgresql
    DB_NAME=seu_nome_do_banco
    DB_USER=seu_usuario_do_banco
    DB_PASSWORD=sua_senha_do_banco
    DB_HOST=localhost
    DB_PORT=5432 # Apenas para PostgreSQL, MySQL etc.
    ALLOWED_HOSTS=localhost,127.0.0.1 # Adicione domínios de produção aqui se DEBUG=False
    ```
    *Lembre-se: O arquivo `.env` não deve ser enviado para o Git.*

5.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
6.  **Crie um superusuário (opcional, para acessar o painel admin):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para criar seu usuário.

7.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    A API estará disponível em `http://127.0.0.1:8000/`.