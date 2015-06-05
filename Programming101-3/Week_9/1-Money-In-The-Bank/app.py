from settings import DB_NAME
from sql_manager import Db

db = Db(DB_NAME)


class Client:

    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")

        while True:
            command = input("$$$>")

            if command == 'register':
                user_credentials = self.getUserInput()
                db.register(user_credentials[0], user_credentials[1])

                print("Registration Successfull")

            elif command == 'login':
                user_credentials = self.getUserInput()

                logged_user = db.login(username, password)

                if logged_user:
                    self.logged_menu(logged_user)
                else:
                    print("Login failed")

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                db.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                db.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")

    def getUserInput(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return(username, password)
