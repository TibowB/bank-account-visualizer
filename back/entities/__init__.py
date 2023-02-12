from .statement import *
from .transaction import *
import datetime

from peewee import Model, CharField, AutoField, SqliteDatabase, DateTimeField, FloatField, ForeignKeyField

db = SqliteDatabase('bov.db')

def init_db():
    db.close()
    db.connect()
    db.drop_tables([Account,Statement])
    db.create_tables([Account,Statement])
    Account.create(account_id="HELLO", routing_number="123", branch_id="456")
    account = Account.get_by_id(1)
    Statement.create(start_date=datetime.datetime.now(),end_date=datetime.datetime.now(), balance=100.0,available_balance=100.0,account=account)

class Account(Model):
    id = AutoField()
    account_id = CharField()
    routing_number = CharField()
    branch_id = CharField()

    class Meta:
        database = db

class Statement(Model):
    id = AutoField()
    start_date = DateTimeField(default=datetime.datetime.now)
    end_date = DateTimeField(default=datetime.datetime.now)
    balance = FloatField()
    available_balance = FloatField()
    account = ForeignKeyField(Account, backref='statements')

    class Meta:
        database = db
