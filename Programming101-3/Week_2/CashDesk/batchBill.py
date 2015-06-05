class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum(self.bills)

    def __getitem__(self, index):
        return self.bills[index]
