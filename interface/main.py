from Menu import *
from User import User

def main():
    LoginMenu = Menu("Welcome to Fantasy Rowing!", ["Login", "Signup", "Quit"])
    
    while True:
        LoginMenu.display()
        choice = LoginMenu.prompt()
        user = False
        if choice == -1:
            return
        elif choice == 1:
            user = login()
        elif choice == 2:
            user = signup()

        if user == False:
            continue

        username = user['username']
        MainMenu = Menu(username, ["Team", "Quit"])
        CurrentUser = User(username)

        while True:
            MainMenu.display()
            choice = MainMenu.prompt()
            if choice == -1:
                break
            if choice == 1:
                CurrentUser.displayTeam()

if __name__ == "__main__":
    main()
