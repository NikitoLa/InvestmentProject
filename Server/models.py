from peewee import *

db = PostgresqlDatabase(database='Investment project', user='postgres', password='12345', host='localhost')


class BaseModel(Model):
    class Meta:
        database = db


class Questions(BaseModel):
    id_question = PrimaryKeyField(unique=True)
    question = TextField()
    target_score = FloatField()

    class Meta:
        order_by = 'id_question'
        db_table = 'questions'


class Indicators(BaseModel):
    id_indicator = PrimaryKeyField(unique=True)
    indicator_question = TextField()

    class Meta:
        order_by = 'id_indicator'
        db_table = 'indicators'
