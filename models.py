import os
from peewee import *
from flask_login import UserMixin

from playhouse.db_url import connect

# establish connection with Heroku
DATABASE = connect(os.environ.get('DATABASE_URL'))

#refactored to be an inherited class for our models
# Model is an inherited parent Class from peewee
class BaseModel(Model):
# Linking the model to the database with class Meta
  class Meta:
    database = DATABASE

class Person(UserMixin, BaseModel):
  personname = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()

class FavedBook(BaseModel):
  person = ForeignKeyField(Person, backref='person')
  title = CharField()
  cover_url = CharField()
  apiKey = CharField()
  has_read = BooleanField()
  recommended = BooleanField()


# establish connection with the tables. If no tables exist, it will create them. safe=True guarantees that existing tables will not be overwritten.
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([FavedBook, Person], safe=True)
  print("TABLES Created")
  DATABASE.close()