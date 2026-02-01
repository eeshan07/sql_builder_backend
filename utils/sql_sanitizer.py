def is_safe_sql(sql: str) -> bool:
    forbidden = ["DROP", "DELETE", "TRUNCATE", "ALTER"]
    sql_upper = sql.upper()
    return not any(word in sql_upper for word in forbidden)
