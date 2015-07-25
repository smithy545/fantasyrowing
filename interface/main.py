import Menu

def main():
    LoginMenu = Menu("Welcome to Fantasy Rowing!", ["Login", "Signup", "Quit"])
    
    while True:
        LoginMenu.display()
        choice = LoginMenu.prompt()
        user = ""
        if choice == "q":
            return
        elif choice == "Login":
            user = login()
        elif choice == "Signup":
            user = signup()

        if user == -1:
            continue

        MainMenu = Menu(user, ["View Team", "Quit"])

        while True:
            MainMenu.display()
            choice = MainMenu.prompt()
            if choice == "q":
                break
            if choice == "View Team":
                CurrentUser.displayTeam()

if __name__ == "__main__":
    main()
