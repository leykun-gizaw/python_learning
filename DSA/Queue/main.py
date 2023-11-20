class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.is_empty()
