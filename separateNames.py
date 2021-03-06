import sqlite3
from types import *

def quotify(s):
    if type(s) == NoneType:
        return '""'
    if type(s) != UnicodeType:
        s = unicode(s)
    return u'"' + s + u'"'

connin = sqlite3.connect("test.db")
connin.row_factory = sqlite3.Row
connout = sqlite3.connect("test2.db")
c1 = connin.cursor()
c2 = connout.cursor()

c2.execute('''CREATE TABLE IF NOT EXISTS viewathlete_athlete (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                first_name varchar(200) NULL,
                last_name varchar(200) NULL,
                age integer NULL,
                height integer NULL,
                weight real NULL,
                gender varchar(1) NULL,
                residence varchar(500) NULL,
                clubs varchar(500) NULL,
                started_rowing integer NULL,
                birth_date date NULL,
                age integer NULL);''')

for r in c1.execute("select * from athlete;"):
    name = r[1].split(" ")
    first_name = name[0].title()
    last_name = name[1].title()
    height = r[2] or 0
    weight = r[3] or 0.0
    gender = r[4]
    residence = r[5]
    clubs = r[6]
    started_rowing = r[7] or 2000
    birth_date = r[8]
    age = r[9] or 0
    items = [quotify(field) for field in [first_name, last_name, height, weight, gender, residence, clubs, started_rowing, birth_date, age]]
    c2.execute(u"INSERT INTO viewathlete_athlete (first_name, last_name, height, weight, gender, residence, clubs, started_rowing, birth_date, age) VALUES(" + u",".join(items) + u");")
    
connout.commit()
connin.close()
connout.close()
