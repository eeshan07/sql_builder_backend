from flask import Blueprint, jsonify
from app.services.metadata_service import get_tables, get_columns

metadata_bp = Blueprint("metadata", __name__)

@metadata_bp.route("/tables", methods=["GET"])
def tables():
    return jsonify(get_tables())

@metadata_bp.route("/tables/<int:table_id>/columns", methods=["GET"])
def columns(table_id):
    return jsonify(get_columns(table_id))
