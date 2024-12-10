from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Lista de objetos para armazenar os itens
items = []

# Definindo o modelo de dados para os itens
class ItemModel:
    def __init__(self, name, value, creation_date, isElectronic):
        self.id = len(items) + 1  # Atribuindo um id ao itens
        self.name = name
        self.value = value
        self.creation_date = creation_date
        self.isElectronic = isElectronic

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "creation_date": self.creation_date,
            "isElectronic": self.isElectronic
        }

# Populando a lista de itens iniciais
items.append(ItemModel("Item 1", 50, "2024-12-10 08:00:00", True))
items.append(ItemModel("Item 2", 56, "2024-12-11 09:00:00", False))
items.append(ItemModel("Item 3", 69, "2024-12-12 10:00:00", True))

# Rota inicial
@app.route('/')
def index():
    return "CRUD API"

# 1. Listar itens
@app.get("/items")
def list_items():
    # Verifica se a lista está vazia
    if not items:
        # Retorna uma mensagem e um status 404 se não houver itens
        return jsonify({"message": "Nenhum item encontrado"}), 404

    return jsonify([item.json() for item in items]), 200

# 2. Salvar item
@app.post("/items")
def save_item():
    item_data = request.get_json()

    # Verificar se todos os campos necessários estão presentes
    if not item_data or "name" not in item_data or "value" not in item_data or "isElectronic" not in item_data:
        return jsonify({"error": "Os campos 'name', 'value' e 'isElectronic' são obrigatórios!"}), 400

    name = item_data["name"]
    value = item_data["value"]
    isElectronic = item_data["isElectronic"]
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_item = ItemModel(name, value, creation_date, isElectronic)
    items.append(new_item)

    return jsonify(new_item.json()), 201

@app.put("/items/<int:item_id>")
def edit_item(item_id):
    # Encontrar o item pela ID
    item = next((item for item in items if item.id == item_id), None)

    if item is None:
        return jsonify({"error": "Item não encontrado"}), 404

    # Atualizar os campos do item
    item_data = request.get_json()
    item.name = item_data.get("name", item.name)
    item.value = item_data.get("value", item.value)
    item.isElectronic = item_data.get("isElectronic", item.isElectronic)

    return jsonify(item.json()), 200

if __name__ == "__main__":
    app.run(debug=True)
