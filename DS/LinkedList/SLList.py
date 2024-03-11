"""Linked list classes"""

from .Node import Node


class SLList:
    """Singly Linked list class"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return

    def get_head(self):
        """Get the head of the linked list

        Returns:
            The head of the list
        """
        return self.head

    def get_tail(self):
        """Get the tail of the linked list

        Returns:
            The head of the list
        """
        return self.tail

    def is_empty(self):
        """Find out if the list is empty

        Returns:
            :attr:`True` if empty, :attr:`False` otherwise
        """
        return self.head is None

    def insert_at_head(self, data):
        """Create and insert a node `new_node` at the head

        Args:
            `data` (Any): Payload to store in node

        Returns:
            Newly created node `new_node`
        """
        new_node = Node(data)

        if self.is_empty() is True:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return new_node

    def insert_at_tail(self, data):
        """Create and insert a node `new_node` at the tail

        Args:
            `data` (Any): Payload to store in node

        Returns:
            Newly created node `new_node`
        """
        new_node = Node(data)

        if self.is_empty() is True:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.length += 1
        self.tail = new_node

        return new_node

    def insert_at_index(self, data, index):
        """Create and insert a node `new_node` at specified index

        Args:
            `data` (Any): Payload to store in node
            `index` (int): Index to insert `new_node` at

        Returns:
            Newly created node `new_node`
        """
        new_node = Node(data)

        if index >= self.length or index < 0:
            raise Exception("Index out of range")
        elif index == 0:
            return self.insert_at_head(data)
        elif index == self.length - 1:
            return self.insert_at_tail(data)

        traverser = self.get_head()
        while index != 1:
            traverser = traverser.next
            index -= 1

        new_node.next = traverser.next
        traverser.next = new_node

        self.length += 1
        return new_node

    def remove_at_head(self):
        """Remove node at head

        Returns:
            Removed node
        """
        if self.is_empty():
            raise Exception("List is empty")

        head = self.head
        self.head = self.head.next

        return head

    def remove_at_tail(self):
        """Remove node at tail

        Returns:
            Removed node
        """
        if self.is_empty():
            raise Exception("List is empty")
        elif self.length == 1:
            tail = self.head

            self.head, self.tail = None, None
            self.length -= 1

            return tail

        traverser = self.get_head()
        while traverser.next.next is not None:
            traverser = traverser.next

        tail = traverser.next

        traverser.next, self.tail = None, traverser
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
        traverser.next = traverser.next.next

        node_at_index.next = None

        return node_at_index

    def __str__(self):
        val = "None"
        if self.is_empty() is False:
            val = ""
            head = self.get_head()

            while head is not None:
                val += "[" + str(head.data) + "]"
                if head.next is None:
                    val += " -> None"
                else:
                    val += " -> "
                head = head.next
        return val

    pass


if __name__ == "__main__":
    sllist = SLList()

    print("-" * 40)
    print("INSERTING NUMBERS 1 TO 5 in ascending order", end="\n\n")
    print("for num in range(1, 5):")
    print("    ", end="")
    print("sllist.insert_at_tail(num)")

    for num in range(1, 6):
        sllist.insert_at_tail(num)

    print("\nCheck insertion")
    assert (
        sllist.__str__() == "[1] -> [2] -> [3] -> [4] -> [5] -> None"
    ), "Should be => [1] -> [2] -> [3] -> [4] -> [5] -> None"
    print("Checks passed", end="\n\n")
    print(sllist)
    print("-" * 40)

    print("-" * 40)
    print("INSERTING NUMBERS 1 TO 5 in descending order", end="\n\n")
    print("for num in range(1, 6):")
    print("    ", end="")
    print("sllist.insert_at_head(num)")

    for num in range(1, 6):
        sllist.insert_at_head(num)

    print("\nCheck insertion")
    assert (
        sllist.__str__() == "[5] -> [4] -> [3] -> [2] -> [1] -> None"
    ), "Should be => [5] -> [4] -> [3] -> [2] -> [1] -> None"
    print("Checks passed", end="\n\n")
    print(sllist)
    print("-" * 40)
