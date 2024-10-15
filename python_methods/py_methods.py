from typing import List, Optional
import datetime
from datetime import date
import time
from typing import NewType, Union, Dict

# define specific data types
PIN = NewType("PIN", int)


class Customer:
    __slots__ = ("_pin", "_id", "_name", "_address", "_mobile_number")
    author: str = "Himasha"
    license: str = "Apache 2.0"

    def __init__(self, id: str, name: str, address: str, mobile_number: int) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._mobile_number = mobile_number
        self._pin: Optional[PIN]

    @staticmethod
    def get_date() -> str:
        return datetime.datetime.today().strftime("%d%m%Y")

    @property
    def name(self) -> str:
        return self._name

    @property
    def pin(self) -> Union[PIN, None]:
        return self._pin

    @pin.setter
    def pin(self, pin_number: PIN) -> str:
        self._pin = pin_number
        return "Pin modified .."

    def return_credits(cls) -> Dict[str, str]:
        return {"author": cls.author, "license": cls.license}


if __name__ == "__main__":
    customer = Customer(
        id="12345",
        name="Himasha",
        address="Gmapaha",
        mobile_number=768464525,
    )

    print(customer.name)
    # set a pin
    cx_pin: PIN = PIN(1234)
    customer.pin = cx_pin

    print("get customer pin", customer.pin)
    print(customer.get_date())
    print(customer.return_credits())
