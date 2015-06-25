from key_node import KeyNode
from heap_with_nodes import Heap


class BandwidthManager:

    def __init__(self):
        self.__queue = Heap()
        self.__priority_manager = {
            "ICMP": 1,
            "UDP": 2,
            "RTM": 3,
            "IGMP": 4,
            "DNS": 5,
            "TCP": 6,
        }

    def rcv(self, protocol, payload):
        if protocol in self.__priority_manager:
            priority = self.__priority_manager[protocol]
            self.__queue.insert(KeyNode(priority, payload))

    def send(self):
        for_sending = self.__queue.delete()
        if for_sending is not None:
            return for_sending.get_value()
        return None


def programm_loop():
    bm = BandwidthManager()
    while True:
        user_input = input('Enter a command: ')
        command = command_parser(user_input, bm)
        if command == 'exit':
            break
        if command is not None:
            print(command)


def command_parser(user_input, bm):
    commands = user_input.split()
    if commands[0] == 'rcv':
        bm.rcv(commands[1], commands[2])
    elif commands[0] == 'send':
        package = bm.send()
        if package is not None:
            return package
        return 'Nothing to send!'
    elif commands[0].lower() == 'exit':
        return 'exit'
    else:
        return 'Invalid command'


def main():
    programm_loop()

if __name__ == '__main__':
    main()
