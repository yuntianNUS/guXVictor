import json
import datetime


class Transaction:
    def __init__(
        self,
        in_type: str,
        value: int,
        is_transfer: bool,
        transfer_details: dict,
        in_date: datetime.datetime,
    ):
        self.__type = in_type
        self.__value = value
        self.__is_tranfer = is_transfer
        self.__transfer_details = transfer_details
        self.__date = in_date

    def get_transaction_type(self) -> str:
        return self.__type

    def get_transaction_value(self) -> int:
        return self.__value

    def get_transaction_is_transfer(self) -> bool:
        return self.__is_tranfer

    def get_transaction_transfer_details(self) -> dict:
        return self.__transfer_details

    def get_transaction_date(self) -> datetime.datetime:
        return self.__date

    def __str__(self):
        return json.dumps(
            {
                "datetime": self.__date,
                "type": self.__type,
                "value": self.__value,
                "is_transfer": self.__is_tranfer,
                "transfer_details": self.__transfer_details,
            }
        )
