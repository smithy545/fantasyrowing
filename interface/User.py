import sqlite3
from helpers import *

class User:
    def __init__(self, username):
        db = getDatabase()
        c = getCursor(db)
        userinfo = c.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()

        self.team = []
        if userinfo["team"]:
            for ID in userinfo["team"].split(";"):
                self.team.append(c.execute("SELECT * FROM rower WHERE\
                                            rower.id = ?;", (ID,)).fetchone())        


        self.league = League(c.execute("SELECT id FROM league WHERE id = ?;", (userinfo["league"],)).fetchone()[0])

        closeDatabase(db)

    def displayTeam(self):
        for i, rower in enumerate(self.team):
            for key in rower.keys():
                print rower[key],
            print ""

class League:
    def __init__(self, leagueID):
        db = getDatabase()
        c = getCursor(db)
        league = c.execute("SELECT * FROM league WHERE id = ?", (leagueID,)).fetchone()

        self.name = league["name"]
        self.userIDs = []
        for user in league["users"].split(";"):
            self.userIDs.append(user)
        closeDatabase(db)

    def availableRowers(self):
        db = getDatabase()
        c = getCursor(db)

        allRowers = c.execute("SELECT * FROM rower;").fetchall()
        for rower in allRowers:
            for userID in self.userIDs:
                temp = c.execute("SELECT team FROM user WHERE user.id = ?;", (userID,)).fetchone()
                if temp:
                    for takenRower in temp[0].split(";"):
                        if int(rower["id"]) == int(takenRower):
                            allRowers.remove(rower)

        closeDatabase(db)
        return allRowers

