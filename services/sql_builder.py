from sqlalchemy import text
from core.database import engine
from core.config import DWH_SCHEMA


def resolve_table(table_id: int) -> str:
    sql = text(f"""
        SELECT table_name, schema_name
        FROM {DWH_SCHEMA}.dwh_tables
        WHERE id = :id
    """)
    with engine.connect() as conn:
        row = conn.execute(sql, {"id": table_id}).fetchone()
        if not row:
            raise ValueError("Invalid table_id")
        return f"{row.schema_name}.{row.table_name}"


def build_sql_from_canvas(canvas: dict) -> str:
    nodes = canvas.get("nodes", [])
    edges = canvas.get("edges", [])
    selected_columns = canvas.get("selectedColumns", [])
    filters = canvas.get("filters", [])

    if not nodes:
        raise ValueError("No tables on canvas")

    base_table_id = nodes[0]["data"]["table_id"]
    base_table = resolve_table(base_table_id)

    select_clause = ", ".join(selected_columns) if selected_columns else "*"
    sql = f"SELECT {select_clause} FROM {base_table}"

    for edge in edges:
        join_type = edge["data"].get("joinType", "INNER").upper()
        join_condition = edge["data"]["on"]
        target_table_id = int(edge["target"])
        target_table = resolve_table(target_table_id)

        sql += f" {join_type} JOIN {target_table} ON {join_condition}"

    if filters:
        sql += " WHERE " + " AND ".join(filters)

    return sql
