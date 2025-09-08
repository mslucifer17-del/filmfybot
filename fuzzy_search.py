from database import db_cursor
from thefuzz import fuzz
from typing import List, Tuple

async def smart_search(query: str, limit: int = 5) -> List[Tuple[str, str]]:
    async with db_cursor() as cur:
        # 1. full-text
        cur.execute("""
            SELECT title, url FROM movies
            WHERE to_tsvector('simple', title) @@ plainto_tsquery('simple', %s)
            LIMIT %s
        """, (query, limit))
        fts = cur.fetchall()
        if fts:
            return fts
        # 2. ilike
        cur.execute("SELECT title, url FROM movies WHERE title ILIKE %s LIMIT %s", (f"%{query}%", limit))
        ilike = cur.fetchall()
        if ilike:
            return ilike
        # 3. fuzz
        cur.execute("SELECT title, url FROM movies")
        all_m = cur.fetchall()
        scored = [(t, u, fuzz.partial_ratio(query.lower(), t.lower())) for t, u in all_m]
        scored = [x for x in scored if x[2] >= 80]
        scored.sort(key=lambda x: x[2], reverse=True)
        return [(t, u) for t, u, _ in scored[:limit]]
