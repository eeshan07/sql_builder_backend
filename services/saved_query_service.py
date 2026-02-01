from sqlalchemy import text
from core.database import engine
from core.config import APP_SCHEMA


def save_query(name: str, sql_text: str, canvas_json: dict):
    sql = text(f"""
        INSERT INTO {APP_SCHEMA}.saved_queries
        (name, sql_text, canvas_json)
        VALUES (:name, :sql, :canvas)
    """)
    with engine.begin() as conn:
        conn.execute(sql, {
            "name": name,
            "sql": sql_text,
            "canvas": canvas_json
        })


def get_saved_queries():
    sql = text(f"SELECT * FROM {APP_SCHEMA}.saved_queries")
    with engine.connect() as conn:
        rows = conn.execute(sql).fetchall()
        return [dict(row._mapping) for row in rows]
