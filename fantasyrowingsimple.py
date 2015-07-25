import hashlib, os, sys

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
            return "q"
        return self.options[choice - 1]

def login():
    print "Login"
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    users = open("users.txt", "r")
    hashes = open("hashes.txt", "r")
    for user in users.read().splitlines():
        if user == username:
            for h in hashes.read().splitlines():
                if int(h) == hash(user + password):
                    print "Login Successful"
                    users.close()
                    hashes.close()
                    return username
            print "Invalid Login"
            return False            

    print "Invalid Login"
    return False
    

def signup():
    print "Signup"

    users = open("users.txt", "r+")
    allUsers = users.readlines()
    
    while True:
        username = raw_input("Enter a username(q to quit): ")
        if username in allUsers:
            print "Username taken. Try Again."
        elif username == "q":
            return -1
        else:
            break
    
    password = raw_input("Enter a password: ")

    hashes = open("hashes.txt","a")
    
    users.write(username + "\n")
    hashes.write(str(hash(username+password)) + "\n")
    return username

  
