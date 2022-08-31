import os
from peewee import *

db_file = f'{os.path.dirname(os.path.abspath(__file__))}/sqlite.db'
db = SqliteDatabase(db_file)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    is_published = BooleanField(default=True)
