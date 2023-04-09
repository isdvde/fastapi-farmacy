from psycopg2 import DatabaseError
from db.config import DB
from string import ascii_lowercase
from random import choice


class Base():
    def __init__(self):
        self.tablename = "tablename"
        self.db = DB()
        self.attr = ()

    def init(self):
        sql = f"""create table {self.tablename} (
                id serial primary key unique not null,
                id_farmacia int not null,
                nombre varchar not null,
                apellido varchar not null,
                edad int not null,
                cargo varchar
                );"""
        self.db.run(sql)

    def randomString(self):
        return ''.join(choice(ascii_lowercase) for i in range(10))

    def initRelations(self, data=[]):
        for key, relation in data:
            sql = f"""
            alter table {self.tablename}
            add constraint {self.randomString()}
            foreign key ({key})
            references {relation}(id)
            on delete cascade
            on update cascade
            """
            self.db.run(sql)

    def drop(self):
        sql = f"drop table if exists {self.tablename} cascade;"
        self.db.run(sql)

    def get(self, id=""):
        if id:
            sql = f"select * from {self.tablename} where id = {id}"
        else:
            sql = f"select * from {self.tablename}"
        return self.db.get(sql)

    def insert(self, attr="", values="", data={}):
        try:
            sql = f"insert into {self.tablename} ({attr}) values ({values})"
            self.db.run(sql, data)
            return True
        except DatabaseError as e:
            print(e)
            return False

    def __del__(self):
        del self.db
