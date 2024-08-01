import sqlite3  # sqlite3 라이브러리를 불러온다.

def read_table_values(db_name, table_name):
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(db_name)  # db_name에 연결한다.
        cursor = conn.cursor()  # 커서를 생성한다.
        
        # 테이블의 모든 값을 조회
        cursor.execute(f"SELECT * FROM {table_name}")  # f-string 포맷팅을 사용해서 table_name을 쿼리에 포함시킨다.
        rows = cursor.fetchall()  # 모든 행을 가져온다.
        
        # 컬럼 이름 가져오기
        cursor.execute(f"PRAGMA table_info({table_name})")  # 테이블 정보 조회
        columns = [info[1] for info in cursor.fetchall()]  # 컬럼 이름 리스트
        
        # 조회된 데이터를 정돈된 형식으로 출력
        formatted_data = {col: {f'a': row[0], f'b': row[1]} for col, row in zip(columns, zip(*rows))}
        
        print(f"{table_name} : {{")  # 테이블 이름 출력
        for col, vals in formatted_data.items():
            print(f"  {col} : {{")  # 컬럼 이름 출력
            for k, v in vals.items():
                print(f"    {k} : {v},")  # 각 값 출력
            print("  },")
        print("}")
        
        print("모든 데이터를 성공적으로 조회했습니다.")  # 조회 성공 메시지를 출력한다.
    except sqlite3.Error as e:  # 예외가 발생하면
        print(f"SQLite 오류: {e}")  # 오류 메시지를 출력한다.
    finally:
        if conn:  # 연결이 되어 있다면
            conn.close()  # 연결을 닫는다.

# 예시 사용법
db_name = '테스트.db'  # 데이터베이스 이름
table_name = '유저'  # 테이블 이름
read_table_values(db_name, table_name)  # 함수를 호출해서 테이블의 모든 값을 조회한다.
