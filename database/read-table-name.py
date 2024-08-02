import sqlite3  # sqlite3 라이브러리를 불러온다.

def get_table_names(db_name: str):
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(db_name)  # db_name에 연결한다.
        cursor = conn.cursor()  # 커서를 생성한다.

        # 모든 테이블 이름 조회
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()  # 모든 테이블 이름을 가져온다.

        return [table[0] for table in tables]  # 테이블 이름 리스트를 반환한다.
    except sqlite3.Error as e:  # 예외가 발생하면
        print(f"SQLite 오류: {e}")  # 오류 메시지를 출력한다.
        return []  # 빈 리스트를 반환한다.
    finally:
        if conn:  # 연결이 되어 있다면
            conn.close()  # 연결을 닫는다.

# 예시 사용법
db_name = '테스트.db'  # 데이터베이스 이름
table_names = get_table_names(db_name)  # 함수 호출해서 테이블 이름을 가져온다.

print("데이터베이스에 있는 테이블들:")
for name in table_names:  # 가져온 테이블 이름들을 반복하면서
    print(name)  # 테이블 이름을 출력한다.
