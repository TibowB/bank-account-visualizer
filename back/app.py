from fastapi import FastAPI, UploadFile
from account import Account
from statement import Statement
from ofxparse import OfxParser
import uvicorn

from security.cors import add_cors_midddleware

app = FastAPI()

add_cors_midddleware(app)

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    ofx = OfxParser.parse(file.file)

    account = Account(ofx.account)

    statement = Statement(account.statement)

    return {"account": account, "statement": statement}

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
