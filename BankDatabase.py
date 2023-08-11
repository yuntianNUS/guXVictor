from Customer import Customer
from Account import Account


class BankDatabase:
    customers = list(Customer)
    accounts = list(Account)

    def __init__(self):
        pass

    def initialise(self):
        for i in range(10):
            customer = Customer
