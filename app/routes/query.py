from flask import Blueprint, request, jsonify
from app.services.sql_builder import build_sql_from_canvas
from app.services.query_executor import execute_sql
from app.utils.sql_sanitizer import is_safe_sql

query_bp = Blueprint("query", __name__)

@query_bp.route("/generate", methods=["POST"])
def generate_sql():
    canvas = request.json
    sql = build_sql_from_canvas(canvas)
    return jsonify({"sql": sql})

@query_bp.route("/execute", methods=["POST"])
def execute():
    sql = request.json.get("sql")
    if not is_safe_sql(sql):
        return jsonify({"error": "Unsafe SQL detected"}), 400
    rows = execute_sql(sql)
    return jsonify(rows)
