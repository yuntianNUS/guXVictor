from Transaction import Transaction

from Customer import Customer


class Account:
    def __init__(self, type, in_account_number, balance, in_customer):
        self.__type = type
        self.__account_number = in_account_number
        self.__balance = balance
        self.__customer = in_customer
        self.__transactions = []

    def get_account_type(self) -> int:
        return self.__type

    def get_account_number(self) -> int:
        return self.__account_number

    def get_account_balance(self) -> int:
        return self.__balance

    def get_account_customer(self) -> Customer:
        return self.__customer

    def get_account_transactions(self) -> list:
        return self.__transactions

    def set_balance(self, new_balance: int) -> int:
        if new_balance >= 0:
            self.__balance = new_balance

    def add_transaction(self, transaction: Transaction) -> None:
        self.__transactions.append(transaction)
