from Customer import Customer
from Account import Account


class BankDatabase:
    customers = []
    accounts = []

    def __init__(self):
        self.initialise()

    def initialise(self):
        for i in range(10):
            customer = Customer(in_name=f"customer{i + 1}", in_customer_id=i + 1)
            self.customers.append(customer)

            account = Account(
                type="SAVINGS",
                in_account_number=(i + 1),
                balance=100,
                in_customer=customer,
            )
            self.accounts.append(account)

    def get_all_customers(self):
        return self.customers.copy()

    def get_all_accounts(self):
        return self.accounts.copy()

    def get_customer_by_id(self, id):
        cus = list(filter(lambda x: x.get_customer_id() == id, self.customers))[0]
        if not cus:
            raise Exception("Customer not found")
        return cus

    def get_account_by_account_number(self, acc_number):
        acc = list(
            filter(lambda x: x.get_account_number() == acc_number, self.accounts)
        )[0]
        if not acc:
            raise Exception("Account not found")
        return acc
