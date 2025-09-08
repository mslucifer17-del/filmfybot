import psycopg2
from psycopg2 import pool          # <-- ये लाइन जोड़ी
from contextlib import asynccontextmanager
from config import DATABASE_URL

db_pool = pool.SimpleConnectionPool(1, 20, DATABASE_URL)   # <-- अब pool. से call

@asynccontextmanager
async def db_cursor():
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        db_pool.putconn(conn)

def init_db():
    with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS movies (id SERIAL PRIMARY KEY, title TEXT UNIQUE, url TEXT);")
            conn.commit()
