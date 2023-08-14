class Customer:
    def __init__(self, in_name: str, in_customer_id: int):
        self.__name = in_name
        self.__customer_id: in_customer_id

    def get_customer_name(self) -> str:
        return self.__name

    def get_customer_id(self) -> int:
        return self.__customer_id
