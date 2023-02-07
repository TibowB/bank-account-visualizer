from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from security.cors import add_cors_midddleware

app = FastAPI()

add_cors_midddleware(app)

class Test(BaseModel):
    name: str

@app.get("/")
async def home():
    return {"json": "Hello World !"}

@app.post("/test")
async def test(test: Test):
    return {"json": test.name}

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
