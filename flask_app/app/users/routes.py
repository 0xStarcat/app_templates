from flask import jsonify
from app.users import bp


@bp.route('/', methods=['GET'])
def index_get():
    return jsonify({})
