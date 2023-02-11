from fastapi import FastAPI, UploadFile
from models import Account, Statement, Transaction
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

    transactions: list[Transaction] = list()

    for transaction in statement.transactions:
        trn = Transaction(transaction)
        transactions.append(trn)

    return {"account": account, "statement": statement, "transactions": transactions}

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
