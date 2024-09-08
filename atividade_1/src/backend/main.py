from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def principal():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)