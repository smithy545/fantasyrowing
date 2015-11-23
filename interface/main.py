from Menu import *
from User import User
from helpers import *

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
        MainMenu = Menu(username, ["View Team", "Edit Team", "Quit"])
        CurrentUser = User(username)

        while True:
            MainMenu.display()
            choice = MainMenu.prompt()
            if choice == -1:
                break
            if choice == 1:
                CurrentUser.displayTeam()
            if choice == 2:
                tempList = []
                for row in CurrentUser.league.availableRowers():
                    tempList.append(str(rowToList(row)))
                tempMenu = Menu("Available Rowers", tempList)
                tempMenu.display()
                rower = tempMenu.prompt()

if __name__ == "__main__":
    main()
