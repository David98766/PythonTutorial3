from userservice.UserService import  UserService
from validation.UserValidation import UserValidation
# the reward now of using good OOP practices we don't have many lines in the main class

# Calling the service layer handling business logic, if made login method static would'nt need to make a userService Object
# Creating a userService Object to access methods of UserService
userService = UserService(UserValidation)

# Calling the login method from UserService
userService.login()