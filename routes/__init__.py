from flask import Blueprint
from routes.item_routes import list_items, save_item, edit_item, remove_item

item_routes = Blueprint('item_routes', __name__)

item_routes.add_url_rule('/items', view_func=list_items, methods=['GET'])
item_routes.add_url_rule('/items', view_func=save_item, methods=['POST'])
item_routes.add_url_rule('/items/<int:item_id>', view_func=edit_item, methods=['PUT'])
item_routes.add_url_rule('/items/<int:id>', view_func=remove_item, methods=['DELETE'])
