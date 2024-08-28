from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def query_db(sql_query: str):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            return [dict(row) for row in result.fetchall()]
    except SQLAlchemyError as e:
        raise RuntimeError(f"Error ejecutando la consulta SQL: {e}")
