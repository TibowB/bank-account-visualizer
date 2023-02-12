from pydantic import BaseModel

class AccountDto(BaseModel):
    account_id: str
    routing_number: str
    branch_id: str