from sqlalchemy import create_engine
from core.config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
