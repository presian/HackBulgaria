from HistoryType import HistoryType


class Account:

    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = []
        self.__make_history('create')

    def deposit(self, money):
        if money <= 0:
            raise ValueError
        self.__balance += money
        self.__make_history('deposit', money)

    def balance(self):
        self.__make_history('check')
        return self.__balance

    def withdraw(self, money):
        if money >= self.__balance or money <= 0:
            self.__make_history("withdraw_failed", money)
            return False
        self.__balance -= money
        self.__make_history("withdraw", money)
        return True

    def currency(self):
        return self.__currency

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}"\
            .format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        self.__make_history("int_check")
        return self.__balance

    def transfer_to(self, account, money):
        if self.__currency != account.currency():
            raise TypeError
        if money >= self.__balance:
            return False
        return True

    def getHistory(self):
        return self.__history

    def __make_history(self, *args):
        action_type = args[0]
        if action_type == "create":
            self.__history.append(HistoryType.CREATED)
        if action_type == "deposit":
            self.__history.append(HistoryType.DEPOSIT.format(args[1], self.__currency))
        if action_type == "withdraw":
            self.__history.append(HistoryType.WITHDRAW.format(args[1], self.__currency))
        if action_type == "withdraw_failed":
            self.__history.append(HistoryType.WITHDRAW_FAILED.format(args[1], self.__currency))
        if action_type == "check":
            self.__history.append(HistoryType.BALANCE_CHECK.format(self.__balance, self.__currency))
        if action_type == "int_check":
            self.__history.append(HistoryType.INT_CHECK.format(self.__balance, self.__currency))
