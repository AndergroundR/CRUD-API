from flask import Flask
from config import Config
from models import db
from routes import routes

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Endpoint inicial da aplicação, retorna 'CRUD API'."""
    return "CRUD API"

if __name__ == "__main__":
    """Executa a aplicação Flask em modo de desenvolvimento."""
    app.run(debug=True)
