from Tutorial_4.userdao.UserDAO import UserDAO
# Creating a service layer for the user class this will handle business logic related to user
# this is an example of MVC (Model View Controller) Good programming practice for website development
class UserService:

    # Creating the login function
    def login(self):

        # Retrieve the list of all users from UserDAO
        userListToCheckAgainst = UserDAO.getAllUsers()

        # Prompt the user for email and password input
        email = input("Enter your Email: ")
        password = input("Enter your password: ")

        # Flag to check if the user is found
        user_found = False

        # Iterate through the list of users to find a matching user
        for user in userListToCheckAgainst:
            if user.userEmail == email and user.userPassword == password:
                user_found = True
                if user.isManager:
                    print("Hello Manager, Welcome Back")
                else:
                    print("Hello Employee, Welcome Back")
                break  # Exit the loop once a user is found

        # If no matching user is found, display an error message
        if not user_found:
            print("Invalid username or password. Try again.")