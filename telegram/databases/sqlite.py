import os
import datetime
from peewee import *

db_file = f'{os.path.dirname(os.path.abspath(__file__))}/sqlite.db'
db = SqliteDatabase(db_file)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = BigIntegerField(unique=True)
    first_name = CharField()
    last_name = CharField(null=True)
    username = CharField(unique=True, null=True)
    language_code = CharField(null=True, default='en')
    is_blocked = BooleanField(default=False)
    acted_at = DateTimeField(default=datetime.datetime.now)
    created_at = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    # db.create_tables([User])
    ...
