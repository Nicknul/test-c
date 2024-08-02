import sqlite3
from typing import List, Dict

def connect_db():
    conn = sqlite3.connect('테스트.db')
    conn.row_factory = sqlite3.Row
    return conn

def search_users_by_name(name: str) -> List[Dict]:
    conn = connect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 유저 WHERE 이름 = ?", (name,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()
