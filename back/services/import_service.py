from ofxparse import OfxParser
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from dtos import AccountDto
from entities import Account, Statement, Transaction

class ImportService:

    def __init__(self, ofx_parser: OfxParser) -> None:
        self.ofx_parser = ofx_parser


    def import_ofx_file(self, file: UploadFile):

        try:
            ofx = self.ofx_parser.parse(file)

            account = self.save_account_from_ofx(ofx)

            statement = self.save_statement_from_ofx(ofx, account)

            self.save_transactions_from_ofx(ofx, statement)

            return JSONResponse(content="Import successful!", status_code=200)
        except:
            return JSONResponse(content="Something wrong happened!", status_code=200)

    def save_account_from_ofx(self, ofx):
        account = ofx.account
        return Account.create(
            account_id=account.account_id, 
            routing_number=account.routing_number, 
            branch_id=account.branch_id)

    def save_statement_from_ofx(self, ofx, account: Account):
        statement = ofx.account.statement
        return Statement.create(
            start_date=statement.start_date,
            end_date=statement.end_date,
            balance=statement.balance,
            available_balance=statement.available_balance,
            account=account)

    def save_transactions_from_ofx(self, ofx, statement: Statement):
        transaction_list = [
            Transaction.create(
                payee = transaction.payee,
                type = transaction.type,
                date = transaction.date,
                amount = transaction.amount,
                tid = transaction.id,
                statement = statement) 
            for transaction in ofx.account.statement.transactions
            ]
        Transaction.bulk_create(transaction_list, batch_size=100)
        