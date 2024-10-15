# define utility calsses
class A:
    def __init__(self) -> None:
        pass

    def methodA(self) -> None:
        print("I'm Method A")


class B:
    def __init__(self) -> None:
        pass

    def methodB(self) -> None:
        print("I'm Method B")


# data structure to keep the objects
class Stack:
    def __init__(self) -> None:
        self.data = []


# define macro class
class Macro:
    def __init__(self) -> None:
        self.a = A()
        self.b = B()
        self.stack = Stack()

    def createMacro(self):
        self.stack.data.append(self.a.methodA)
        self.stack.data.append(self.b.methodB)

    def executeMacro(self):
        self.createMacro()

        for x in self.stack.data:
            x.__call__()


if __name__ == "__main__":
    obj = Macro()
    obj.executeMacro()
