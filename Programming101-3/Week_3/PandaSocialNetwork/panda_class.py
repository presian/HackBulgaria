import re
from panda_error import InvalidEmail


class Panda():

    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = self.__email_validator(email)
        self.__gender = gender

    def gender(self):
        return self.__gender

    def email(self):
        return self.__email

    def name(self):
        return self.__name

    def isMale(self):
        if self.__gender == "male":
            return True
        return False

    def isFemale(self):
        if self.__gender == "female":
            return True
        return False

    def __eq__(self, other):
        return self.__name == other.__name\
            and self.__email == other.__email\
            and self.__gender == other.__gender

    def __hash__(self):
        return hash(self.__name)

    def __str__(self):
        return "Name: {}\nEmail: {}\nGender: {}"\
            .format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return self.__str__()

    def __email_validator(self, email):
        pattern = "^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if re.match(pattern, email):
            return email
        raise InvalidEmail
