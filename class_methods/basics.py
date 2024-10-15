"""
Instance, Class, and Static Methods
"""


class MyClass:
    def method(self):
        """
        Through the self parameter, instance methods can freely access attributes and other methods on the same object.
        This gives them a lot of power when it comes to modifying an object’s state.

        Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute.
        This means instance methods can also modify class state.
        """

        return "instance method called", self

    @classmethod
    def classmethod(cls):
        """
        Because the class method only has access to this cls argument, it can’t modify object instance state.
        That would require access to self. However, class methods can still modify class state that applies across all instances of the class.
        """

        return "class method called", cls

    @staticmethod
    def staticmethod():
        """
        Therefore a static method can neither modify object state nor class state.
        Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
        """

        return "static method called"


# Class Method Use Case 1 : factory design method
"""
As you can see, we can use the factory functions to create new Pizza objects that are configured the way we want them. 
They all use the same __init__ constructor internally and simply provide a shortcut for remembering all of the various ingredients.

Another way to look at this use of class methods is that they allow you to define alternative constructors for your classes.

Python only allows one __init__ method per class. Using class methods it’s possible to add as many alternative constructors as necessary. 
This can make the interface for your classes self-documenting (to a certain degree) and simplify their usage.
"""


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
