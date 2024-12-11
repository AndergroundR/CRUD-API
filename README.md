# CRUD API - Gerenciamento de Itens

Esta é uma API desenvolvida com Flask e SQLAlchemy que permite realizar operações CRUD (Listar, Salvar, Alterar e Deletar) em um banco de dados de objetos. 

## Tecnologias Utilizadas

- Python 3.12
- Flask
- Flask-SQLAlchemy
- SQLite 

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/AndergroundR/CRUD-API.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd CRUD-API
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Crie o banco de dados e as tabelas:
    ```bash
    python crud.py
    ```

6. A API estará rodando em https://crud-api-609039858016.us-central1.run.app/

## Endpoints da API

### 1. **Listar todos os itens**

- **Endpoint:** `GET https://crud-api-609039858016.us-central1.run.app/items`
- **Descrição:** Lista todos os itens cadastrados no banco de dados.
- **Resposta de Sucesso (200):**
    ```json
    [
    {
    "creation_date": "2024-12-10 21:59:05",
    "id": 1,
    "isElectronic": false,
    "name": "Item 1",
    "value": 10.0
    },
        ...
    ]
    ```

### 2. **Criar um item**

- **Endpoint:** `POST https://crud-api-609039858016.us-central1.run.app/items`
- **Descrição:** Cria um novo item no banco de dados.
- **Body:**
    ```json
    {
    "name": "Item 4",
    "value": 40,
    "isElectronic": true
    }
    ```
- **Resposta de Sucesso (201):**
    ```json
    {
        "id": 4,
        "name": "Item 4",
        "value": 40,
        "isElectronic": true,
        "creation_date": "2024-12-10 12:30:00"
    }
    ```



### 3. **Atualizar um item**

- **Endpoint:** `PUT https://crud-api-609039858016.us-central1.run.app/items/{id}`
- **Descrição:** Atualiza os dados de um item específico baseado no ID.
- **Body:**
    ```json
    {
        "name": "Novo nome do item alterado",
        "value": 150,
        "isElectronic": false
    }
    ```
- **Resposta de Sucesso (200):**
    ```json
    {
        "id": 1,
        "name": "Novo nome do item",
        "value": 150,
        "isElectronic": false,
        "creation_date": "2024-12-10 12:30:00"
    }
    ```

### 4. **Deletar um item**

- **Endpoint:** `DELETE https://crud-api-609039858016.us-central1.run.app/items/{id}`
- **Descrição:** Deleta um item pelo ID.
- **Resposta de Sucesso (200):**
    ```json
    {
        "message": "Item removido com sucesso"
    }
    ```
## Testes

Os testes da API foram implementados utilizando o **pytest**. Para rodar os testes, siga os passos abaixo:

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute os testes com o seguinte comando:
    ```
    pytest
    ```

Os testes estão localizados na pasta `tests/` e validam as funcionalidades principais da API.
