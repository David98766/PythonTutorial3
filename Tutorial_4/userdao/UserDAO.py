from Tutorial_4.model.User import User

# class to hold all users in memory, using this instead of database
class UserDAO:

    # Function is static so that it can be accessed without an object of the class
    # this method is a getter to grab all users but also creates them usually this will grab users from a database
    @staticmethod
    def getAllUsers():
        userList = []

        userManager = User("John", "Doe", "John@gmail.com", "pw1", True)
        userEmployee = User("Daniel", "Doe", "Daniel@gmail.com", "pw2", False)

        userList.append(userManager)
        userList.append(userEmployee)

        return userList