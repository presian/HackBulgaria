from bst import BST


class PhoneBook:

    def __init__(self):
        self.__phonebook = BST()

    def insert(self, number, name):
        entry = self.__phonebook.lookup(name)
        if entry is None:
            self.__phonebook.insert(name, [number])
        else:
            value = entry.get_value()
            value.append(number)

    def lookup(self, name):
        entry = self.__phonebook.lookup(name)
        if entry is not None:
            print('{}: [{}]'.format(entry.get_key(), entry.get_value()))
        else:
            print("NOT FOUND!")

    def list(self):
        all_entries = self.__phonebook.traverse(1)
        for e in all_entries:
            print('{}: [{}]'.format(e[0], ', '.join(e[1])))

    def remove(self, name):
        self.__phonebook.remove(name)


def main():
    pb = PhoneBook()
    pb.insert('1234', "pepo")
    pb.insert('1234', "pepo")
    pb.insert('1234', "gogo")
    pb.insert('1234', "gogo")
    pb.insert('1234', "shosho")
    pb.insert('1234', "shosho")

    # pb.lookup("pepo")
    # pb.list()
    pb.remove('pepo')
    pb.list()

if __name__ == '__main__':
    main()
