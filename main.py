from peewee import *
import sqlite3


db = SqliteDatabase('my_database.db')


class Button(Model):
    mass = FloatField()

    class Meta:
        database = db
        db_table = 'buttons'


class Top(Model):
    mass = FloatField()
    K = FloatField()
    B = FloatField()
    my_button = Button()

    class Meta:
        database = db
        db_table = 'tops'


class Bottom(Model):
    mass = FloatField()
    K = FloatField()
    B = FloatField()
    class Meta:
        database = db
        db_table = 'bottoms'


class Rim(Model):
    mass = FloatField()
    K = FloatField()
    B = FloatField()
    class Meta:
        database = db
        db_table = 'rims'


class Box(Model):
    my_top = Top()
    my_bottom = Bottom()
    my_rim = Rim()

    class Meta:
        database = db
        db_table = 'boxes'


def sql_try():
    db.connect()
    db.create_tables([Box, Top, Button, Bottom, Rim])



# yea
if __name__ == '__main__':
    sql_try()
