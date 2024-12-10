from flask import Flask, request, jsonify


app = Flask(__name__)

# Lista de objetos para armazenar os itens
items = []


# Definindo o modelo de dados para os itens
class ItemModel:
    def __init__(self, id, name, value, creation_date, isElectronic):
        self.id = id
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

# Populando a lista de itens com alguns dados iniciais
items.append(ItemModel(1, "Item 1", 50, "2024-12-10 08:00:00", True))
items.append(ItemModel(2, "Item 2", 56, "2024-12-11 09:00:00", False))
items.append(ItemModel(3, "Item 3", 69, "2024-12-12 10:00:00", True))

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

if __name__ == "__main__":
    app.run(debug=True)
