from flask import jsonify


def json_list(data):
    return jsonify({"data": data, "count": len(data)})
