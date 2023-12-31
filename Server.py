from BankDatabase import BankDatabase
from Account import Account
from Transaction import Transaction
from datetime import datetime


class Server:
    def __init__(self):
        self.bank_db = BankDatabase()

    def get_cus_name_from_acc_num(self, account_number: int) -> int:
        account: Account = self.bank_db.get_account_by_account_number(account_number)
        return account.get_account_customer().get_customer_name()

    def show_balance(self, account_number: int) -> int:
        account: Account = self.bank_db.get_account_by_account_number(account_number)
        return account.get_account_balance()

    def get_last_ten_transactions(self, account_number) -> int:
        account: Account = self.bank_db.get_account_by_account_number(account_number)
        return account.get_account_transactions()[:10]

    def create_new_transaction(
        self,
        account: Account,
        transaction_type,
        value,
        is_transfer,
        transfer_details,
    ) -> Transaction:
        new_transaction = Transaction(
            in_type=transaction_type,
            value=value,
            is_transfer=is_transfer,
            transfer_details=transfer_details,
            in_date=str(datetime.now()),
        )
        account.add_transaction(new_transaction)
        return new_transaction

    def withdraw_balance(
        self, account_number: int, withdraw_value: int, is_transfer, transfer_details
    ):
        account: Account = self.bank_db.get_account_by_account_number(
            acc_number=account_number
        )
        if withdraw_value < 1:
            raise ValueError("Please enter more than 1 to withdraw")

        if account.get_account_balance() >= withdraw_value:
            print(f"Withdrawing {withdraw_value}...")
            new_balance = account.get_account_balance() - withdraw_value
            account.set_balance(new_balance)
            self.create_new_transaction(
                account=account,
                transaction_type="CR",
                value=withdraw_value,
                is_transfer=is_transfer,
                transfer_details=transfer_details,
            )
            return account.get_account_balance()
        else:
            raise ValueError("Not enough balance")

    def deposit_balance(
        self, account_number: int, value: int, is_transfer, transfer_details
    ):
        account: Account = self.bank_db.get_account_by_account_number(
            acc_number=account_number
        )

        if value > 0:
            new_balance = account.get_account_balance() + value
            account.set_balance(new_balance)
            self.create_new_transaction(
                account=account,
                transaction_type="CR",
                value=value,
                is_transfer=is_transfer,
                transfer_details=transfer_details,
            )
            return account.get_account_balance()
        else:
            raise ValueError("Please deposit more than 0")

    def transfer_funds(
        self, from_account_number: int, to_account_number: int, value: int
    ):
        if value < 1:
            raise ValueError("Please enter amount >= 1")
        try:
            from_account = self.bank_db.get_account_by_account_number(
                from_account_number
            )  # credit
            to_account = self.bank_db.get_account_by_account_number(
                to_account_number
            )  # deposit
        except Exception as e:
            print(e)

        try:
            from_transfer_details = {"transfer_to": to_account_number, "value": value}
            to_transfer_details = {"transfer_from": from_account_number, "value": value}

            self.withdraw_balance(
                from_account_number, value, True, from_transfer_details
            )
            self.deposit_balance(to_account_number, value, True, to_transfer_details)

            # self.create_new_transaction(
            #     account=from_account,
            #     transaction_type="CR",
            #     value=value,
            #     is_transfer=True,
            #     transfer_details={"transfer_to": to_account_number, "value": value},
            # )  # from account

            # self.create_new_transaction(
            #     account=to_account,
            #     transaction_type="DR",
            #     value=value,
            #     is_transfer=True,
            #     transfer_details={"transfer_from": from_account_number, "value": value},
            # )
            return from_account.get_account_balance()

        except Exception as e:
            print(e)
