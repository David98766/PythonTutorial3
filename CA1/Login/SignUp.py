from Login.userservice.UserService import UserService
from Login.validation.UserValidation import UserValidation

userValidation = UserValidation

userService = UserService(userValidation)

userService.signUp()