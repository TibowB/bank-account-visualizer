import datetime

from peewee import Model, CharField, AutoField, SqliteDatabase, DateTimeField, FloatField, ForeignKeyField

db = SqliteDatabase('bov.db')

def init_db():
    db.close()
    db.connect()
    db.drop_tables([Account,Statement, Transaction])
    db.create_tables([Account,Statement, Transaction])

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

class Transaction(Model):
    id = AutoField()
    payee = CharField()
    type = CharField()
    date = DateTimeField()
    amount = FloatField()
    tid = CharField()   
    statement = ForeignKeyField(Statement, backref='transactions')

    class Meta:
        database = db
