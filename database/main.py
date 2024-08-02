import sqlite3  # sqlite3 라이브러리를 불러온다.
from fastapi import FastAPI, HTTPException  # FastAPI와 HTTP 예외처리를 불러온다.
from pydantic import BaseModel  # pydantic 라이브러리에서 BaseModel을 불러온다.
from fastapi.middleware.cors import CORSMiddleware  # CORS 설정을 위해 CORSMiddleware를 불러온다.
from typing import List  # 리스트 타입을 불러온다.

app = FastAPI()  # FastAPI 앱을 생성한다.

# CORS 설정 추가
origins = [
    "http://localhost:3001",  # Next.js 애플리케이션의 주소
    "http://127.0.0.1:3001"   # Next.js 애플리케이션의 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    name: str  # name 필드는 문자열 타입이다.

class UserDTO(BaseModel):
    이름: str  # 이름 필드는 문자열 타입이다.
    아이디: str  # 아이디 필드는 문자열 타입이다.
    비밀번호: int  # 비밀번호 필드는 정수 타입이다.

@app.post("/search", response_model=List[UserDTO])  # /search 경로로 POST 요청을 처리한다.
async def search_users(request: SearchRequest):  # 요청 데이터를 SearchRequest 객체로 받는다.
    try:
        conn = sqlite3.connect('테스트.db')  # 데이터베이스 연결
        conn.row_factory = sqlite3.Row  # 행을 딕셔너리 형식으로 가져오도록 설정한다.
        cursor = conn.cursor()  # 커서를 생성한다.
        
        # 이름이 일치하는 행을 검색한다.
        cursor.execute("SELECT * FROM 유저 WHERE 이름 = ?", (request.name,))
        rows = cursor.fetchall()  # 모든 행을 가져온다.
        
        if not rows:  # 행이 없다면
            raise HTTPException(status_code=404, detail="User not found")  # 404 예외를 발생시킨다.
        
        users = [UserDTO(**dict(row)) for row in rows]  # 각 행을 UserDTO 객체로 변환한다.
        return users  # 유저 리스트를 반환한다.
    except sqlite3.Error as e:  # 예외가 발생하면
        raise HTTPException(status_code=500, detail=str(e))  # 500 예외를 발생시킨다.
    finally:
        if conn:
            conn.close()  # 연결을 닫는다.


if __name__ == "__main__":
    import uvicorn  # uvicorn 라이브러리를 불러온다.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)  # uvicorn 서버를 시작한다. 
