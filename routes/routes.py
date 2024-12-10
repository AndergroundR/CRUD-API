from flask import request, jsonify
from datetime import datetime
from models.models import db, ItemModel

def list_items():
    """
        Obter todos os itens no banco de dados.

        parametros: Nenhum.
        resposta: Lista de todos os itens.

    """
    items = ItemModel.query.all()

    if not items:
        return jsonify({"message": "Nenhum item encontrado"}), 404

    return jsonify([item.json() for item in items]), 200

def save_item():
    """
        Criar um novo item no banco de dados.

        parametros: item_data (Detalhes do item para salvar).
        resposta: Dados do item criado.

    """
    item_data = request.get_json()

    if not item_data or "name" not in item_data or "value" not in item_data or "isElectronic" not in item_data:
        return jsonify({"error": "Os campos 'name', 'value' e 'isElectronic' são obrigatórios!"}), 400

    name = item_data["name"]
    value = item_data["value"]
    isElectronic = item_data["isElectronic"]
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_item = ItemModel(name, value, creation_date, isElectronic)
    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.json()), 201

def edit_item(item_id):
    """
        Atualizar um item existente pelo ID.

        parametros: item_id (ID do item a ser atualizado), item_data (Campos a serem atualizados).
        resposta: Dados do item atualizado.

    """
    item = ItemModel.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    item_data = request.get_json()
    item.name = item_data.get("name", item.name)
    item.value = item_data.get("value", item.value)
    item.isElectronic = item_data.get("isElectronic", item.isElectronic)

    db.session.commit()
    return jsonify(item.json()), 200

def remove_item(id):
    """
        Deletar um item pelo ID.

        parametros: id (ID do item a ser deletado).
        resposta: Mensagem de sucesso.

    """
    item = ItemModel.query.get(id)

    if not item:
        return jsonify({"erro": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item removido com sucesso"}), 200
