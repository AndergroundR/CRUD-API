from flask import Blueprint
from routes.routes import list_items, save_item, edit_item, remove_item

routes = Blueprint('routes', __name__)

routes.add_url_rule('/items', view_func=list_items, methods=['GET'])
routes.add_url_rule('/items', view_func=save_item, methods=['POST'])
routes.add_url_rule('/items/<int:item_id>', view_func=edit_item, methods=['PUT'])
routes.add_url_rule('/items/<int:id>', view_func=remove_item, methods=['DELETE'])
