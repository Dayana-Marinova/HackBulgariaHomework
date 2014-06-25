import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")
        command_array = command.split(" ")
        if command == 'register':
            username = input("Enter your username: ")
            email = input('Enter your email: ')
            while True:
                password = getpass.getpass()
                if len(password) < 8:
                    print("Your Pasword is to short, it must be 8 symbols")
                elif not have_upper_letters(password):
                    print("Your password must have upper letters")
                elif not number_function(password):
                    print("Your password must have numbers")
                elif not have_special(password):
                    print("It must have special symbols")
                elif username in password:
                    print("Don`t use your name in your password")
                else:
                    sql_manager.register(username, sql_manager.get_crypted(password), email)
                    break
            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")

            logged_user = sql_manager.login(username, sql_manager.wrong_password_count(username))

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'send-reset-password':
            username = input("Enter your username: ")
            print(sql_manager.send_reset_password(username))

        elif command_array[0] == 'reset-password':
            print(sql_manager.reset_password(command_array[1]))

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass()
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")

        elif command == 'deposit':
            amount = input('Enter amount: ')
            tan = input('Enter code: ')
            print(sql_manager.deposit(logged_user.get_username(), amount, tan))

        elif command == 'withdraw':
            amount = input('Enter amount: ')
            tan = input('Enter code: ')
            print(sql_manager.withdraw(logged_user.get_username(), amount. tan))

        elif command == 'display':
            print(sql_manager.get_balance(logged_user.get_username()))

        elif command == 'get-tan':
            password = getpass.getpass()
            print(sql_manager.generate_tan_codes(logged_user.get_username(), password))

        else:
            print("Not a valid command")


def number_function(password):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in password:
        if i in number:
            return True
    return False


def have_special(password):
    special_symbols = ['?', '!', "'", '.', '^', "#", "$", '*', '+', '-', '_', '|', '(', ')', '@']
    for i in password:
        if i in special_symbols:
            return True
    return False


def have_upper_letters(password):
    for i in password:
        if i == i.upper():
            return True
    return False


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
