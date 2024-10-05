# defining a class for a user this encapsulates all data a user can have
class User:

    # Constructor to initalise the user class needs these parameters
    def __init__(self, firstName, lastName, userEmail, userPassword, isManager):

        self.firstName = firstName
        self.lastName = lastName
        self.userEmail = userEmail
        self.userPassword = userPassword
        self.isManager = isManager
