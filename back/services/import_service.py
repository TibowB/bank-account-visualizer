from ofxparse import OfxParser
from fastapi import UploadFile

from entities import Account, Statement, Transaction

class ImportService:

    def __init__(self, ofx_parser: OfxParser) -> None:
        self.ofx_parser = ofx_parser

    def import_ofx_file(self, file: UploadFile):
        ofx = self.ofx_parser.parse(file)

        account = Account(ofx.account)

        statement = Statement(account.statement)

        transactions: list[Transaction] = list()

        for transaction in statement.transactions:
            trn = Transaction(transaction)
            transactions.append(trn)
            
        return {"account": account, "statement": statement, "transactions": transactions}