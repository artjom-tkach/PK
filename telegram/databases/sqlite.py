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


class Category(BaseModel):
    # Language titles
    title_en = CharField()
    title_ru = CharField()
    # Language description
    description_en = CharField()
    description_ru = CharField()

    image = CharField(null=True)
    parent = ForeignKeyField('self', backref='children', null=True, on_delete='SET NULL')

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)


class Product(BaseModel):
    # Language titles
    title_en = CharField()
    title_ru = CharField()
    # Language description
    description_en = CharField()
    description_ru = CharField()

    image = CharField(null=True)

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    # db.drop_tables([Category])
    db.create_tables([User, Category])
