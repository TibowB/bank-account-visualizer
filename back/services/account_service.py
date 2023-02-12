from entities import Account
from dtos import AccountDto
from peewee import DoesNotExist, IntegrityError
from typing import List

class AccountService:

    def __init__(self, entity: Account) -> None:
        self.entity = entity

    def get_all_accounts(self) -> List[AccountDto]:
        return [account for account in self.entity.select().dicts()]

    def get_account_by_id(self, id: int) -> AccountDto:
        try:
            return self.entity.get_by_id(id)
        except DoesNotExist:
            return None
    
    def update_account_by_id(self, id: int, dto: AccountDto):
        query = self.entity.update(
        account_id=dto.account_id,
        routing_number=dto.routing_number,
        branch_id=dto.branch_id).where(self.entity.id == id)
        
        updated_rows = query.execute()

        if updated_rows == 0:
            return f"Account with id {id} does not exist"
    
        return dto

    def add_account(self, dto: AccountDto):
        try:
            return self.entity.create(account_id = dto.account_id, routing_number = dto.routing_number,branch_id = dto.branch_id)
        except IntegrityError:
            return "None field can be null"

    def delete_account_by_id(id: int) -> str:
        deleted_rows = Account.delete_by_id(id)
    
        if deleted_rows == 0:
            return f"Can't delete account with id {id}, it doesn't exist"

        return "Delete successful"