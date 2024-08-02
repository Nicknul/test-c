import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('테스트.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 유저 테이블에서 모든 데이터를 조회
cursor.execute("SELECT * FROM 유저")
rows = cursor.fetchall()

for row in rows:
    print(dict(row))  # 각 행을 딕셔너리로 변환하여 출력

conn.close()
