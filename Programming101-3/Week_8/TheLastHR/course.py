class Course:

    def __init__(self, name, group):
        self.group = group
        self.name = name

    def __str__(self):
        return "Name: {}, Group: {}".format(self.name, self.group)

    def __repr__(self):
        return self.__str__()
