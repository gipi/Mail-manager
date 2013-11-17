from peewee import *
import psycopg2
import sys

database = PostgresqlDatabase(None)

def init_db(username, password, dbname):
    database.init(dbname, **{
        'host': 'localhost',
        'user': username,
        'password': password,
    })
    try:
        database.connect()
    except psycopg2.OperationalError as e:
        print e.message
        sys.exit(1)

def create_table():
    Users.create_table()


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
