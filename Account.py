from Transaction import Transaction


class Account:
    type: "SAVINGS"
    account_number: -1
    balance = 0
    transactions: list(Transaction) = []

    def __init__(self, type, in_account_number, balance):
        self.type = type
        self.account_number = in_account_number
        self.balance = balance
