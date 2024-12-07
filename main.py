from peewee import *


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
    my_button = ForeignKeyField(Button, backref='top')

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
    my_top = ForeignKeyField(Top, backref='box')
    my_bottom = ForeignKeyField(Bottom, backref='box')
    my_rim = ForeignKeyField(Rim, backref='box')

    class Meta:
        database = db
        db_table = 'boxes'


def sql_try():
    db.connect()
    db.create_tables([Box, Top, Button, Bottom, Rim], safe=True)

    new_button = Button.create(mass=.1)
    new_button2 = Button.create(mass=.15)
    new_top = Top.create(mass=.3, K=100000, B=12, my_button=new_button2)
    new_top2 = Top.create(mass=.25, K=110000, B=10, my_button=new_button)
    new_back = Bottom.create(mass=0.25, K=120000, B=2)
    new_back2 = Bottom.create(mass=0.27, K=125000, B=2.5)
    new_rim = Rim.create(mass=0.65, K=12000, B=200)
    new_box = Box.create(my_top=new_top, my_bottom=new_back, my_rim=new_rim)
    new_box2 = Box.create(my_top=new_top2, my_bottom=new_back2, my_rim=new_rim)

    db.close()

# yea
if __name__ == '__main__':
    sql_try()
