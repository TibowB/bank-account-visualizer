class Account:

    def __init__(self, account) -> None:
        self.account_id = account.account_id
        self.routing_number = account.routing_number
        self.branch_id = account.branch_id    
        self.institution = account.institution

    def __str__(self) -> str:
        return f"{self.account_id} {self.routing_number} {self.branch_id}"