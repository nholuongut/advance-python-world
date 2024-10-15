"""
SOLID design principles
    S - single responsibility model
        each class or method should have a single responsibility,if not then devide the
        class or method into sub classes or methods
        
    O - open-closed principle
        methods or classes should be available for extension but closed for
        modifications
        
    L - Liskov substitution
        if you have objects inside a program , you should be able to
        substitude them with their subtypes, sub classes without violating correctness
        of the programm
        
    I - interface seggregation
        it's always better to have a specialized interfaces than common general interafce
        
    
    D - dependancy inversion
        classes should depend on abstractions , not on concreate subclasses
    
"""
from abc import ABC, abstractmethod, abstractproperty


class OrderBase(ABC):
    @abstractmethod
    def add_item(self, name: str, quantity: int, price: float):
        pass

    @abstractmethod
    def total_price(self):
        pass

    def set_status(self, status: str) -> None:
        pass


class Order(OrderBase):
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float):
        self.items.append(name)  # type: ignore
        self.quantities.append(quantity)  # type: ignore
        self.prices.append(price)  # type: ignore

    def total_price(self) -> float:  # type: ignore
        total: float = 0
        for i in range(len(self.prices)):  # type: ignore
            total += self.quantities[i] * self.prices[i]  # type: ignore
        return total  # type: ignore

    def set_status(self, status: str):
        self.status = status


### interface seggragtion
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False
        super().__init__()

    def pay(self, order: OrderBase):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status("paid")

    def auth_sms(self, code: str):
        print(f"Verifying SMS code : {code}")
        self.verified = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code
        self.verified = False
        super().__init__()

    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email: str) -> None:
        self.email = email
        self.verified = False
        super().__init__()

    def pay(self, order: OrderBase):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing credit payment type")
        print(f"Verifying email address code: {self.email}")
        order.set_status("paid")

    def auth_sms(self, code: str):
        print(f"Verifying SMS code : {code}")
        self.verified = True


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())

payment_method = DebitPaymentProcessor(security_code="0372846")
payment_method.auth_sms(code="1234")
payment_method.pay(order=order)
