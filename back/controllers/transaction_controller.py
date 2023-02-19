from app import app
from entities import Transaction
from dtos import TransactionDto
from typing import List

@app.get('/transaction')
async def get_all_transactions():
    transactions = [transaction for transaction in Transaction.select().dicts()]
    print(transactions)
    return {"transactions": transactions}