from BankDatabase import BankDatabase
from Account import Account
from Transaction import Transaction


class Server:
    def __init__(self):
        self.bank_db = BankDatabase()

    def show_balance(self, account_number: int):
        account: Account = self.bank_db.get_account_by_account_number(account_number)
        return account.balance

    def create_new_transaction(
        self, account: Account, transaction_type, value, is_transfer, transfer_details
    ) -> Transaction:
        new_transaction = Transaction(
            in_type=transaction_type,
            value=value,
            is_transfer=is_transfer,
            transfer_details=transfer_details,
        )
        account.add_transaction(new_transaction)
        return new_transaction

    def withdraw_balance(self, account_number: int, withdraw_value: int):
        account: Account = self.bank_db.get_account_by_account_number(
            acc_number=account_number
        )
        if account.balance >= withdraw_value:
            print(f"Withdrawing {withdraw_value}...")
            new_balance = account.balance - withdraw_value
            account.set_balance(new_balance)
            self.create_new_transaction(
                account=account,
                transaction_type="CR",
                value=withdraw_value,
                is_transfer=False,
                transfer_details={},
            )
            return account.balance
        # else:
        #     raise ValueError("Not enough balance")

    def deposit_balance(self, account_number: int, value: int):
        account: Account = self.bank_db.get_account_by_account_number(
            acc_number=account_number
        )

        if value > 0:
            new_balance = account.balance + value
            account.set_balance(new_balance)
            self.create_new_transaction(
                account=account,
                transaction_type="CR",
                value=value,
                is_transfer=False,
                transfer_details={},
            )
            return account.balance
        else:
            raise ValueError("Please deposit more than 0")

    def transfer_funds(
        self, from_account_number: int, to_account_number: int, value: int
    ):
        try:
            from_account = self.bank_db.get_account_by_account_number(
                from_account_number
            )  # credit
            to_account = self.bank_db.get_account_by_account_number(
                to_account_number
            )  # deposit
        except Exception as e:
            print(e)

        # try:
        self.withdraw_balance(from_account_number, value)
        self.deposit_balance(to_account_number, value)

        self.create_new_transaction(
            account=from_account,
            transaction_type="CR",
            value=value,
            is_transfer=True,
            transfer_details={"transfer_to": to_account_number, "value": value},
        )
        self.create_new_transaction(
            account=from_account,
            transaction_type="DR",
            value=value,
            is_transfer=True,
            transfer_details={"transfer_from": to_account_number, "value": value},
        )
        return from_account.balance

        # except Exception as e:
        #     print(e)
