"""""
state design pattern is valuable when you have a class object with different state levels
and each state comes with specific implementation
if we are going to implement all the states inside single class , then we are not
accormodating SOLID design pattern
"""

from typing import Protocol, List
from dataclasses import dataclass


class DocumentState(Protocol):
    def edit(self):
        ...

    def review(self):
        ...

    def finalize(self):
        ...


class DocumentContext(Protocol):
    content: List[str]

    def set_state(self, state: DocumentState):
        ...

    def edit(self):
        ...

    def review(self):
        ...

    def finalize(self):
        ...

    def show_content(self):
        ...


# define each state classes
@dataclass
class Draft:
    document: DocumentContext

    def edit(self):
        print("editing the document ...")
        self.document.content.append("Eddited content !")

    def review(self):
        print("document reviwing ...")
        self.document.set_state(Review(self.document))

    def finalize(self):
        print("document should be review first !!!")


@dataclass
class Review:
    document: DocumentContext

    def edit(self):
        print("document in review stage , no edit access ...")

    def review(self):
        print("document in review stage ...")

    def finalize(self):
        print("finalizing the document ...")
        self.document.set_state(Finalize(self.document))


@dataclass
class Finalize:
    document: DocumentContext

    def edit(self):
        print("document in finalized state , no edit access ...")

    def review(self):
        print("document in finalize stage , review already done ...")

    def finalize(self):
        print("document in finalize state ...")


class Document:
    def __init__(self) -> None:
        self.state: DocumentState = Draft(self)
        self.content: List[str] = []

    def set_state(self, state: DocumentState):
        self.state = state

    def edit(self):
        self.state.edit()

    def review(self):
        self.state.review()

    def finalize(self):
        self.state.finalize()

    def show_content(self):
        print(" ".join(self.content))


if __name__ == "__main__":
    # intialize the document
    doc = Document()

    # first edit the document
    doc.edit()
    doc.finalize()
    doc.review()
    doc.edit()
    doc.finalize()
    doc.review()
