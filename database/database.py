import sqlite3  # sqlite3 라이브러리를 불러온다.
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

def get_table_names(db_name: str) -> List[str]:
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()
        return [table[0] for table in tables]
    except sqlite3.Error as e:
        print(f"SQLite 오류: {e}")
        return []
    finally:
        if conn:
            conn.close()
