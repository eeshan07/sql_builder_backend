from sqlalchemy import Table, Column, Integer, String, Text, MetaData

metadata = MetaData()

saved_queries = Table(
    "saved_queries",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("sql", Text),
    Column("canvas_json", Text)
)


