from app import app
from entities import Account
from dtos import AccountDto
from services import AccountService


account_service = AccountService(Account)

@app.get("/account")
async def get_all_accounts():
    return account_service.get_all_accounts()

@app.get("/account/{id}")
async def get_account_by_id(id: int):
    return account_service.get_account_by_id(id)

@app.put("/account/{id}")
async def update_account_by_id(id: int, dto: AccountDto):
    return account_service.update_account_by_id(id, dto)

@app.post("/account")
async def add_account(dto: AccountDto):
    return account_service.add_account(dto)

@app.delete("/account/{id}")
async def delete_account_by_id(id: int):
    return account_service.delete_account_by_id(id)