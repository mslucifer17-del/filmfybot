import psycopg2
from psycopg2 import pool
from contextlib import asynccontextmanager
import asyncio
from config import DATABASE_URL

db_pool = psycopg2.pool.SimpleConnectionPool(1, 20, DATABASE_URL)

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
            cur.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL UNIQUE,
                    url TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_requests (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT,
                    movie_title TEXT,
                    requested_at TIMESTAMP DEFAULT NOW()
                )
            """)
            conn.commit()
