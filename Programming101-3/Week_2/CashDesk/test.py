from bill import Bill
from batchBill import BatchBill
from cahs_desk import CashDesk

# a = Bill(10)
# b = Bill(5)
# c = Bill(10)

# print(int(a) == 10)
# print(str(a) == "A 10$ bill")
# print(a)  # A 10$ bill

# print(a == b)  # False
# print(a == c)  # True

# money_holder = {}

# money_holder[a] = 1  # We have one 10% bill

# if c in money_holder:
#     money_holder[c] += 1

# print(money_holder)  # { "A 10$ bill": 2 }


# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]


# batch = BatchBill(bills)

# for bill in batch:
#     print(bill)


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total)
print(desk.inspect())
