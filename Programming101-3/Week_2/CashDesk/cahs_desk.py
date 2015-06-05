class CashDesk:

    def __init__(self):
        self.total = 0
        self.bills = []

    def take_money(self, bills):
        if bills.__class__.__name__ == "Bill":
            self.bills.append(bills)
        else:
            self.bills.extend(bills)
        self.total = sum([int(bill) for bill in self.bills])

    def total(self):
        return "We have a total of {}$ in the desk".format(self.total)

    def inspect(self):
        list_bills = {bill: self.bills.count(bill) for bill in self.bills}
        return "\n".join(["{} - {}".format(key, list_bills[key]) for key in list_bills])
