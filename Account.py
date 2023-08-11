from Transaction import Transaction

from Customer import Customer


class Account:
    type: "SAVINGS"
    account_number: -1
    balance = 0
    customer: Customer = None

    def __init__(self, type, in_account_number, balance, in_customer):
        self.type = type
        self.account_number = in_account_number
        self.balance = balance
        self.customer = in_customer
        self.transactions = []

    def set_balance(self, new_balance: int):
        if new_balance >= 0:
            self.balance = new_balance

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)
