import psycopg2

from app.models import User


def get_db_connection(user: User):
    conn = psycopg2.connect(
        host=user.host,
        database=user.database_name,
        user=user.username,
        password=user.password,
        port=user.port,
    )
    return conn
