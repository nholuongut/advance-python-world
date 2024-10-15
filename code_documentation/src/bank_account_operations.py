"""Bank account system that emulate bank account and operations betweem them."""

from __future__ import annotations  # * To allow type hints

from datetime import datetime
from enum import StrEnum, auto
from typing import List, Optional


class TransactionType(StrEnum):
    """Represents several operation types in or between bank accounts."""

    DEPOSIT = auto()
    WITHDRAWAL = auto()
    TRANSFER = auto()


Transaction = tuple[TransactionType, datetime, int]


class InsufficientBalanceError(Exception):
    ...


class BankAccount:
    """Represent a bank account entity"""

    def __init__(self, name: str, address: str, initial_balance: int = 0) -> None:
        self._balance = initial_balance
        self._name = name
        self._address = address
        self._transaction_history: list[Transaction] = []

    def deposit(self, amount: int) -> None:
        """send money to the account

        Args:
            amount (int): amount cent in dollars
        """
        self._balance += amount
        self._transaction_history.append(
            (TransactionType.DEPOSIT, datetime.now(), amount)
        )

    def withdraw(self, amount: int) -> None:
        """withdraw money amount from account

        Args:
            amount (int): amount in dollars

        Raises:
            InsufficientBalanceError: error is amount > total balance
        """
        if self._sufficient_balance(amount):
            self._balance -= amount
            self._transaction_history.append(
                (TransactionType.WITHDRAWAL, datetime.now(), amount)
            )
        else:
            raise InsufficientBalanceError

    def transfer(self, other: BankAccount, amount: int) -> None:
        """transfer money amount to another bank

        Args:
            other (BankAccount): recieving party account
            amount (int): amount in dollars

        Raises:
            InsufficientBalanceError: error is amount > total balance
        """
        if self._sufficient_balance(amount):
            timestamp: datetime = datetime.now()
            self._balance -= amount
            other._balance += amount
            # ! Can't append operation at other instance class
            self._transaction_history.append(
                (TransactionType.TRANSFER, timestamp, amount)
            )
        else:
            raise InsufficientBalanceError

    def _sufficient_balance(self, amount: int) -> bool:
        """balance checker against request dollar amount

        Args:
            amount (int): request dollar amount

        Returns:
            bool: return True if amount <= balance else otherwise
        """
        return amount <= self._balance

    @property
    def balance(self) -> int:
        """current account balance

        Returns:
            int: balance in dollars
        """
        return self._balance

    @property
    def transaction_history(self) -> list[Transaction]:
        """all the previous transcations

        Returns:
            list[Transaction]: list of transactions
        """
        # ? Should this be exposed as a read-only property or not?
        return self._transaction_history

    @property
    def account_details(self) -> List[str]:
        """get account holder details

        Returns:
            List[str]: return name/address of the account holder
        """
        return [self._name, self._address]

    @account_details.setter
    def account_details(self, name: Optional[str], address: Optional[str]) -> str:
        """set account holder details

        Args:
            name (Optional[str]): holder name
            address (Optional[str]): holder address

        Returns:
            str: detail change status address
        """
        status: str = ""

        if name is not None:
            self._name = name
        else:
            status += "kindly provide correct name \n"

        if address is not None:
            self._address = address
        else:
            status += "kindly provide correct address"

        return status

    @account_details.deleter
    def account_details(self) -> None:
        """remove account holder details"""
        del self._name
        del self._address


def main() -> None:
    account1 = BankAccount(name="Himasha", address="winnipeg", initial_balance=100)
    account2 = BankAccount(name="Thamali", address="winnipeg", initial_balance=50)

    account1.transfer(account2, 50)

    print(account1.balance)


if __name__ == "__main__":
    main()
