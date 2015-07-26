import sqlite3

class User:
    def __init__(self, username):
        database = sqlite3.connect("rowers.db")
        c = database.cursor()
        teamids = c.execute("SELECT team.rowers FROM team, user WHERE team.id = user.teamid;").fetchone()

        self.team = []
        if teamids:
            for ID in teamids[0].split(";"):
                self.team.append(c.execute("SELECT * FROM rower WHERE rower.id = ?;", (ID)).fetchone())        

    def displayTeam(self):
        for rower in self.team:
                print rower
