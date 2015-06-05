class Student:

    def __init__(self, github, available, name, courses):
        self.github = github
        self.available = available
        self.name = name
        self.courses = courses

    def __str__(self):
        return "Github: {}, Available: {}, Name: {}, Courses: {}".format(self.github, self.available, self.name, self.courses)

    def __repr__(self):
        return self.__str__()
