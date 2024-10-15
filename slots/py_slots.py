"""
    Slots in Python is a special mechanism that is used to reduce memory of the objects. 
    In Python, all the objects use a dynamic dictionary for adding an attribute. 
    Slots is a static type method in this no dynamic dictionary are required for allocating attribute.
"""
from typing import Optional, List
from enum import Enum, auto


class Transactions(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()
    DISABLE = auto()
    CHANGE_PIN = auto()
    CHANGE_NAME = auto()


class BankAccount:
    """python slots create static memeory for object attributed which is saving of RAM
    otherwise normally classes keep dynamic dictionary to keep attributes and slots are more faster to get data
    """

    __slots__ = ("_account_number", "_holder_name", "_pin")

    def __init__(self, account_number: int, holder_name: str, pin: int) -> None:
        self._account_number = account_number
        self._holder_name = holder_name
        self._pin = pin

    @property
    def pin(self) -> int:
        """account pin

        Returns:
            int: return account pin number
        """
        return self._pin

    @property
    def account_number(self) -> int:
        """account number

        Returns:
            int: return account number
        """
        return self._account_number

    @pin.deleter
    def pin(self) -> None:
        del self._pin

    def set_pin(self, new_pin: int, method: Transactions) -> str:
        """set new pin number

        Args:
            new_pin (int): new pin number
            method (Transactions): transaction type (CHANGE_PIN)

        Returns:
            str: pin change status
        """
        if method == Transactions.CHANGE_PIN:
            self._pin = new_pin
            return "pin edit success"
        else:
            return "pin edit failed"


if __name__ == "__main__":
    account = BankAccount(
        account_number=123456,
        holder_name="Himasha",
        pin=1234,
    )

    print(account.__slots__)

    account.set_pin(1234545, Transactions.CHANGE_PIN)
    print(account.account_number)
    del account.pin
    print(Transactions.DEPOSIT.name, Transactions.DEPOSIT.value)
    print(account.__slots__)
    print(account.pin)
