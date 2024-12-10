from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

# Definindo o modelo de dados para os itens
class ItemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    value = db.Column(db.Float, nullable=False)
    creation_date = db.Column(db.String(30), nullable=False)
    isElectronic = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, value, creation_date, isElectronic):
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

# Inicializando o banco de dados
with app.app_context():
    db.create_all()  # Criando tabelas

# Rota inicial
@app.route('/')
def index():
    return "CRUD API"

# 1. Listar itens
@app.get("/items")
def list_items():
    items = ItemModel.query.all()  # Consulta todos os itens no banco

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
    db.session.add(new_item)  # Adiciona o novo item ao banco
    db.session.commit()  # Salva a alteração no banco


    return jsonify(new_item.json()), 201


@app.put("/items/<int:item_id>")
def edit_item(item_id):
    item = ItemModel.query.get(item_id)  # Busca o item pelo id no banco

    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    # Atualizar os campos do item
    item_data = request.get_json()
    item.name = item_data.get("name", item.name)
    item.value = item_data.get("value", item.value)
    item.isElectronic = item_data.get("isElectronic", item.isElectronic)

    db.session.commit()
    return jsonify(item.json()), 200

# 4. Remover item
@app.delete("/items/<int:id>")
def remove_item(id):
    item = ItemModel.query.get(id)

    if not item:
        return jsonify({"erro": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()

    # Retornamos uma mensagem de sucesso
    return jsonify({"message": "Item removido com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)
