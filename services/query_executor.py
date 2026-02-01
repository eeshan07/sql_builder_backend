from sqlalchemy import text
from core.database import engine


def execute_sql(sql: str):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        columns = result.keys()
        return [dict(zip(columns, row)) for row in result.fetchall()]
