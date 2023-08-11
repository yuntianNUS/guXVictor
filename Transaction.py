class Transaction:
    value: 0
    is_transfer = False
    transfer_details: {}

    def __init__(
        self, in_type: str, value: int, is_transfer: bool, transfer_details: dict
    ):
        self.type = in_type
        self.value = value
        self.is_tranfer = is_transfer
        self.transfer_details = transfer_details
