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

def search_data_by_table_and_name(table: str, name: str) -> List[Dict]:
    conn = connect_db()
    try:
        cursor = conn.cursor()

        # 테이블의 컬럼 이름들을 조회한다
        cursor.execute(f"PRAGMA table_info({table})")
        columns_info = cursor.fetchall()
        column_names = [col['name'] for col in columns_info]

        # '이름' 컬럼이 테이블에 있는지 확인한다
        if '이름' in column_names:
            query = f"SELECT * FROM {table} WHERE 이름 = ?"
            cursor.execute(query, (name,))
        else:
            # '이름' 컬럼이 없으면 기본적인 검색 쿼리를 사용한다
            query = f"SELECT * FROM {table} WHERE {column_names[0]} = ?"
            cursor.execute(query, (name,))
        
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()
