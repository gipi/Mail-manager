from peewee import *
import psycopg2
import sys

database = None

def init_db():
    username = raw_input('username ? ')
    password = raw_input('password? ')

    database = PostgresqlDatabase('maildb', **{
        'host': 'localhost',
        'user': username,
        'password': password,
    })
    try:
        database.connect()
    except psycopg2.OperationalError as e:
        print e.message
        sys.exit(1)

init_db()

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Users(BaseModel):
    domain   = CharField()
    gid      = IntegerField(default=8)
    home     = CharField()  
    password = CharField()
    uid      = IntegerField(default=8)
    userid   = CharField()

    class Meta:
        db_table = 'users'
