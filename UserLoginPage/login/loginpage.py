# User array where each sublist contains [username, password, Boolean] - Boolean indicates if manager
users = [['manager', 'pw1', True], ['employee', 'pw2', False]]


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Iterate through the users array to find a matching user
    for user in users:
        if username == user[0] and password == user[1]:
            if user[2] == True:  # Check if the user is a manager
                print("Whats up manager? \n")
            else:  # If not a manager, welcomes the employee
                print("Staff view\n")
            return  # Exit after a successful login

    # Error screen for wrong login credentials
    print("Invalid username or password. Try again.")


login()