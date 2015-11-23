import sqlite3

def getDatabase():
    conn = sqlite3.connect("rowers.db")
    conn.row_factory = sqlite3.Row
    return conn

def getCursor(db):
    return db.cursor()

def closeDatabase(db):
    db.close()

def rowToList(row):
    out = []
    for key in row.keys():
        out.append(row[key])
    return out

def rowsToList(rows):
    out = []
    for row in rows:
        out.append(rowToList(row))
    return out
