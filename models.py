from enum import unique
from peewee import *


db = SqliteDatabase('data.db')


class BaseModel(Model):

    class Meta:
        database = db


class Purchase(BaseModel):

    id = CharField(unique=True)

    class Meta:
        primary_key = False


class KeyWord(BaseModel):

    word = CharField(unique=True)