class Statement:

    def __init__(self, statement) -> None:
        self.start_date = statement.start_date
        self.end_date = statement.end_date
        self.balance = statement.balance
        self.available_balance = statement.available_balance 
        self.transactions = statement.transactions  
    
    def __str__(self) -> str:
        return f"{self.start_date} {self.end_date} {self.balance} {self.available_balance}"