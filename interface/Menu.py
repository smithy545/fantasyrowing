import sqlite3

class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        print self.title
        for i, option in enumerate(self.options):
            print str(i + 1) + ". " + str(option)

    def prompt(self, msg = "? "):
        choice = 0
        while choice < 1 or choice > len(self.options):
            try:
                choice = input(msg)
            except Exception:
                pass
            if choice < 1 or choice > len(self.options):
                print "Invalid choice"

        if self.options[choice - 1].lower() in ("quit", "q", "exit", "leave"):
            return -1
        return choice

def login():
    print "Login"
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    conn = sqlite3.connect("rowers.db")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    for user in c.execute("SELECT * FROM user;"):
        if user['username'] == username and user['hash'] == hash(username + password):
                conn.close()
                print "Login Successful"
                return user        

    conn.close()
    print "Invalid Login"
    return False
    

def signup():
    print "Signup"

    takennames = []

    conn = sqlite3.connect("rowers.db")
    conn.row_factory == sqlite3.Row
    c = conn.cursor()
    for username in c.execute("SELECT username FROM user;"):
        takennames.append(username[0])
    
    while True:
        username = raw_input("Enter a username(q to quit): ")
        if username in takennames:
            print "Username taken. Try Again."
        elif username == "q":
            return False
        else:
            break
    
    password = raw_input("Enter a password: ")
    h = hash(username + password)

    c.execute("INSERT INTO user (username, hash) values (?,?);", (username, h))
    user = c.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()

    conn.commit()
    conn.close()
    
    return user

