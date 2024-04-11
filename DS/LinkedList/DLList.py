"""Module defines a singly linked class"""
from .Node import Node
from .SLList import SLList


class DLList(SLList):
    """Doubly Linked List Class"""

    def __init__(self):
        super().__init__()

    def insert_at_head(self, data):
        new_node = Node(data, set_previous_pointer=True)

        if self.head is not None:
            new_node.next = self.head

        if self.tail is None:
            self.tail = new_node

        self.head = new_node
        self.length += 1

        return new_node

    def insert_at_tail(self, data):
        new_node = Node(data, set_previous_pointer=True)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        new_node.prev = self.tail

        self.tail = new_node
        self.length += 1

        return new_node

    def insert_at_index(self, data, index):
        new_node = Node(data, set_previous_pointer=True)

        if self.is_empty():
            raise Exception("List is empty")
        elif index >= self.length:
            raise Exception("Index out of range")
        elif index < 0:
            raise Exception("Negative indices not allowed")

        traverser = self.get_head()

        while index != 1:
            traverser = traverser.next
            index += 1

        new_node.next = traverser.next
        new_node.prev = traverser

        traverser.next.prev = new_node
        traverser.next = new_node

        self.length += 1

        return new_node
            
    def remove_at_head(self):
        head = self.get_head()
        if head is None:
            raise Exception("List is empty")

        self.head = self.head.next
        self.head.prev = None

        head.next = None
        self.length -= 1

        return head

    def remove_at_tail(self):
        tail = self.get_tail()
        if tail is None:
            raise Exception("List is empty")

        new_tail = tail.prev
        new_tail.next = None

        tail.prev = None
        self.tail = new_tail
        
        self.length -= 1

        return tail

    def remove_at_index(self, index):
        """Remove node at specified index 

        Args:
            `index` (int): Index of node to remove

        Returns:
            Removed node
        """
        if self.is_empty():
            raise Exception("List is empty")

        if index >= self.length:
            raise Exception("Index out of range")

        if index == 0:
            return self.remove_at_head()

        traverser = self.get_head()
        while index != 1:
            traverser = traverser.next
            index -= 1

        node_at_index = traverser.next
        traverser.next.next.prev = traverser
        traverser.next = traverser.next.next

        node_at_index.next = None
        node_at_index.prev = None

        self.length -= 1

        return node_at_index

    def __str__(self):
        val = ""
        if self.is_empty() is False:
            head = self.get_head()

            while head is not None:
                val += "[" + str(head.data) + "]"
                if head.next is None:
                    val += " -> None"
                else:
                    val += " -> <- "
                head = head.next
        return val
    pass


if __name__ == "__main__":
    lst = DLList()
    for num in range(15):
        lst.insert_at_tail(num)
    
    print(lst)
