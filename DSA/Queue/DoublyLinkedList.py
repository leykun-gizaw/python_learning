class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.prev: Node = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail = None
        self.length = 0
        return

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def is_empty(self):
        return self.head != None

    def __str__(self):
        val = ""
        if self.is_empty() is True:
            return val

        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next

        while temp is not None:
            val = val + str(temp.data) + ", "
            temp = temp.next
        val = val + str(temp.data) + "]"
        return val
