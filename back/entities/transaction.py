class Transaction:

    def __init__(self, transaction) -> None:
        self.payee = transaction.payee
        self.type = transaction.type
        self.date = transaction.date
        self.user_date = transaction.user_date
        self.amount = transaction.amount
        self.id = transaction.id
        self.memo = transaction.memo
        self.sic = transaction.sic
        self.mcc = transaction.mcc
        self.checknum = transaction.checknum

    def __str__(self) -> str:
        return f"{self.payee} {self.amount}"