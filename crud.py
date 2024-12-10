from flask import Flask

app = Flask(__name__)

# Lista de objetos para armazenar os itens
items = []


# Definindo o modelo de dados para os itens
class ItemModel:
    def __init__(self, item.id, name, value, creation_date, isElectronic):
        self.id = item.id
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


# Rota inicial
@app.route('/')
def index():
    return "CRUD API"



if __name__ == "__main__":
    app.run(debug=True)
