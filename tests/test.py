import pytest
from crud import app
from models import db, ItemModel

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_item(client):
    """
        #1.

        Descrição: Caso de teste para criar um novo item com dados válidos.

        resposta: Código de status 201. / Retorno dos dados do item com nome correto.

    """
    data = {
        "name": "Item 1",
        "value": 50,
        "isElectronic": True
    }

    response = client.post('/items', json=data)

    assert response.status_code == 201

    json_data = response.get_json()
    assert json_data['name'] == "Item 1"
    assert json_data['value'] == 50
    assert json_data['isElectronic'] is True

def test_get_items(client):
    """
        #2.

        Descrição: Caso de teste para listar todos os itens no banco de dados.

        resposta: Código de status 200. / Retorno da lista de itens.
    """
    data = {
        "name": "Item 2",
        "value": 100,
        "isElectronic": False
    }
    client.post('/items', json=data)

    response = client.get('/items')

    assert response.status_code == 200

    json_data = response.get_json()
    assert len(json_data) > 0
    assert json_data[0]['name'] == "Item 2"

def test_update_item(client):
    """
        #3.

        Descrição: Caso de teste para atualizar um item pelo ID.

        resposta: Código de status 200. / Retorno dos dados do item atualizado.

    """
    data = {
        "name": "Item 3",
        "value": 150,
        "isElectronic": True
    }
    response = client.post('/items', json=data)
    item_id = response.get_json()['id']

    updated_data = {
        "name": "Item 3 Atualizado",
        "value": 200,
        "isElectronic": False
    }
    response = client.put(f'/items/{item_id}', json=updated_data)

    assert response.status_code == 200

    json_data = response.get_json()
    assert json_data['name'] == "Item 3 Atualizado"
    assert json_data['value'] == 200
    assert json_data['isElectronic'] is False

def test_delete_item(client):
    """
        #4.

        Descrição: Caso de teste para deletar um item pelo ID.

        resposta: Código de status 200. / Retorno de mensagem de sucesso.

    """
    data = {
        "name": "Item 4",
        "value": 300,
        "isElectronic": True
    }
    response = client.post('/items', json=data)
    item_id = response.get_json()['id']

    response = client.delete(f'/items/{item_id}')

    assert response.status_code == 200

    response = client.get(f'/items/{item_id}')
    assert response.status_code == 404
