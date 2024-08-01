import sqlite3  # sqlite3 라이브러리를 불러온다.

def create_table(db_name, table_name, name, id, password):
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(db_name)  # db_name에 연결한다.
        cursor = conn.cursor()  # 커서를 생성한다.
        
        # 테이블 생성
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (  
            {name} TEXT NOT NULL,
            {id} TEXT NOT NULL,
            {password} INTEGER NOT NULL
        )
        ''')
        print(f"테이블 '{table_name}'가 성공적으로 생성되었습니다.")  # f-string 포맷팅을 사용해서 출력 메시지에 table_name을 포함시킨다.
        
        # 데이터 삽입
        cursor.execute(f'''
        INSERT INTO {table_name} ({name}, {id}, {password})
        VALUES ('이연승', 'admin1', 1234),
               ('정호연', 'admin2', 5678)
        ''')
        print("데이터가 성공적으로 삽입되었습니다.")  # 데이터가 성공적으로 삽입되었음을 출력한다.
        
        # 변경사항 저장
        conn.commit()  # 변경사항을 저장한다.
    except sqlite3.Error as e:  # 예외가 발생하면
        print(f"SQLite 오류: {e}")  # 오류 메시지를 출력한다.
    finally:
        if conn:  # 연결이 되어 있다면
            conn.close()  # 연결을 닫는다.

# 예시 사용법
db_name = '테스트.db'  # 데이터베이스 이름
table_name = '유저'  # 테이블 이름
name = '이름'  # 컬럼 이름
id = '아이디'  # 컬럼 아이디
password = '비밀번호'  # 컬럼 비밀번호
create_table(db_name, table_name, name, id, password)  # 함수를 호출해서 테이블을 생성하고 데이터를 삽입한다.
