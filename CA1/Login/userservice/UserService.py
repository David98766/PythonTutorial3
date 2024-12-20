from Login.userdao.UserDAO import UserDAO
from Login.validation.UserValidation import UserValidation
from Login.model.User import User
# Creating a service layer for the user class this will handle business logic related to user
# this is an example of MVC (Model View Controller) Good programming practice for website development
class UserService:

    def __init__(self, userValidation):
        # Create an instance of UserDAO to handle user data
        self.userDAO = UserDAO([])  # Passing an empty list to UserDAO constructor
        self.userValidation = userValidation

    # Creating the login function
    def login(self, userEmail, userPassword):

        # Retrieve the list of all users from UserDAO
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # Prompt the user for email and password input
        email = userEmail
        password = userPassword

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


    def signUp(self):
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if self.userValidation.checkEmail(self.userDAO.getAllUsers(), email) and self.userValidation.checkPassword(password):
            userToCreate = User(firstName, lastName, email, password)
            self.userDAO.createUser(userToCreate)
            print(f"Hello {firstName} {lastName}, your account has been created successfully!")
            for user in self.userDAO.getAllUsers():
                print(user)
        else:
            print("Sign up failed. Please try again.")
            self.signUp()  # Recursive call if validation fails