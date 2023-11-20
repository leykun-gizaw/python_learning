"""Module defines a linked list node

It provides a means to create a node for a doubly linked or a singly linked
list.
"""

class Node:
    """A single node unit class"""
    def __init__(self, data, set_previous_pointer=False) -> None:
        self.data = data
        self.next: Node = None
        self.__is_DLL = False

        if set_previous_pointer:
            self.prev: Node = None
            self.__is_DLL = True
        return

    def __repr__(self):
        type = "DLL" if self.__is_DLL else "SLL"
        return f"{type} - [Data = {self.data}]"
