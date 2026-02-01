from flask import Flask, request, jsonify
from flask_cors import CORS

from services.metadata_service import get_tables, get_columns
from services.sql_builder import build_sql_from_canvas
from services.query_executor import execute_sql
from services.saved_query_service import save_query, get_saved_queries
from utils.sql_sanitizer import is_safe_sql

app = Flask(__name__)
CORS(app)

# ---------- METADATA ----------

@app.route("/api/metadata/tables", methods=["GET"])
def tables():
    return jsonify(get_tables())


@app.route("/api/metadata/tables/<int:table_id>/columns", methods=["GET"])
def columns(table_id):
    return jsonify(get_columns(table_id))


# ---------- QUERY BUILDER ----------

@app.route("/api/query/generate", methods=["POST"])
def generate_query():
    canvas = request.json
    sql = build_sql_from_canvas(canvas)
    return jsonify({"sql": sql})


@app.route("/api/query/execute", methods=["POST"])
def execute_query():
    sql = request.json.get("sql")
    if not is_safe_sql(sql):
        return jsonify({"error": "Unsafe SQL detected"}), 400
    return jsonify(execute_sql(sql))


# ---------- SAVED QUERIES ----------

@app.route("/api/saved-query", methods=["POST"])
def save_sql():
    data = request.json
    save_query(
        name=data["name"],
        sql_text=data["sql"],
        canvas_json=data["canvas"]
    )
    return jsonify({"message": "Query saved"})


@app.route("/api/saved-query", methods=["GET"])
def list_saved():
    return jsonify(get_saved_queries())


if __name__ == "__main__":
    app.run(debug=True)
