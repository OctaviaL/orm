# ORM (Object Relational Mapping) - объектно реляционное отображение - технология, которая связывает БД с концепциями обектно - ориетнированных языков программирования.  ORM - прослойка между БД и кодом, который пишет программист, которая позволяет создвать в программе объекты, обновлять, удалять и получать их.

# python: 
    # peeweee
    # sqlalchemy
    # djangoORM

# Класс - таблица в БД
# Атрибут класса - поле в БД
# Объект класса - строка в таблице

from views import *
from settings import db

db.connect()

get_categories()
get_products()


db.close()






