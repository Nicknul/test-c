import sqlite3  # sqlite3 라이브러리를 불러온다.
from pydantic import BaseModel  # pydantic 라이브러리에서 BaseModel을 불러온다.
from typing import List  # 리스트 타입을 불러온다.

class UserDTO(BaseModel):
    이름: str  # 이름 필드는 문자열 타입이다.
    아이디: str  # 아이디 필드는 문자열 타입이다.
    비밀번호: int  # 비밀번호 필드는 정수 타입이다.

def read_table_values(db_name, table_name) -> List[UserDTO]:
    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(db_name)  # db_name에 연결한다.
        conn.row_factory = sqlite3.Row  # 행을 딕셔너리 형식으로 가져오도록 설정한다.
        cursor = conn.cursor()  # 커서를 생성한다.
        
        # 테이블의 모든 값을 조회
        cursor.execute(f"SELECT * FROM {table_name}")  # f-string 포맷팅을 사용해서 table_name을 쿼리에 포함시킨다.
        rows = cursor.fetchall()  # 모든 행을 가져온다.
        
        # 조회된 데이터를 객체 형식으로 가공
        results = [UserDTO(**row) for row in rows]  # 각 행을 UserDTO 객체로 변환하여 리스트에 추가한다.
        
        print("모든 데이터를 성공적으로 조회하고 가공했습니다.")  # 조회 및 가공 성공 메시지를 출력한다.
        return results  # 결과 리스트를 반환한다.
    except sqlite3.Error as e:  # 예외가 발생하면
        print(f"SQLite 오류: {e}")  # 오류 메시지를 출력한다.
        return []  # 빈 리스트를 반환한다.
    finally:
        if conn:  # 연결이 되어 있다면
            conn.close()  # 연결을 닫는다.

# 예시 사용법
db_name = '테스트.db'  # 데이터베이스 이름
table_name = '유저'  # 테이블 이름
users = read_table_values(db_name, table_name)  # 함수를 호출해서 테이블의 모든 값을 조회하고 가공한다.

for user in users:  # 조회된 각 유저를 반복한다.
    print(user)  # 유저 객체를 출력한다.
