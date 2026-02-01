from flask import Blueprint, request, jsonify
from app.services.saved_query_service import save_query, get_saved_queries, update_query

saved_query_bp = Blueprint("saved_query", __name__)

@saved_query_bp.route("/", methods=["POST"])
def save():
    data = request.json
    save_query(data["name"], data["sql"], data["canvas_json"])
    return jsonify({"message": "Saved successfully"})

@saved_query_bp.route("/", methods=["GET"])
def fetch():
    return jsonify(get_saved_queries())

@saved_query_bp.route("/<int:query_id>", methods=["PUT"])
def update(query_id):
    data = request.json
    update_query(query_id, data["name"], data["sql"], data["canvas_json"])
    return jsonify({"message": "Updated successfully"})
