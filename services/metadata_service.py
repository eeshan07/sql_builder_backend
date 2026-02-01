from sqlalchemy import text
from core.database import engine
from core.config import DWH_SCHEMA


def get_tables():
    sql = text(f"""
        SELECT id, table_name, schema_name, table_metadata
        FROM {DWH_SCHEMA}.dwh_tables
    """)
    with engine.connect() as conn:
        rows = conn.execute(sql).fetchall()
        return [dict(row._mapping) for row in rows]


def get_columns(table_id: int):
    sql = text(f"""
        SELECT table_metadata
        FROM {DWH_SCHEMA}.dwh_tables
        WHERE id = :id
    """)
    with engine.connect() as conn:
        row = conn.execute(sql, {"id": table_id}).fetchone()
        if not row:
            return {}
        return row.table_metadata.get("columns", {})
