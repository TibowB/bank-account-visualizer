from pydantic import BaseModel
from datetime import datetime

class AccountDto(BaseModel):
    account_id: str
    routing_number: str
    branch_id: str

class TransactionDto(BaseModel):
    payee: str
    type: str
    date: datetime
    amount: float
    tid: str