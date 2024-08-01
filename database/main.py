from fastapi import FastAPI  # FastAPI 라이브러리를 불러온다.

app = FastAPI()  # FastAPI 앱을 생성한다.

@app.get("/")  # 웹 브라우저에서 주소 뒤에 '/'를 입력하면 이 함수가 실행된다.
def read_root():
    return {"Hello": "World"}  # 웹 브라우저에 {"Hello": "World"}라는 메시지를 보여준다.

if __name__ == "__main__":
    import uvicorn  # uvicorn 라이브러리를 불러온다.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)  # uvicorn 서버를 시작한다. 
