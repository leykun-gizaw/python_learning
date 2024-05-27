"""Module defines a Queue class"""

from ..LinkedList.DLList import DLList

class Queue:
    def __init__(self):
        self.items = DLList()
        pass

    def is_empty(self):
        """Determine if Queue is empty"""
        return self.items.is_empty()

    def front(self):
        """Get the front of the queue"""
        return self.items.get_head()

    def rear(self):
        """Get the rear of the queue"""
        return self.items.get_tail()

    def enqueue(self, element):
        """Enqueue an element into the queue DS

        Args:
            element (Any): Element to enqueue

        Returns:
            Enqueued element
        """
        return self.items.insert_at_tail(element)

    def dequeue(self):
        """Dequeue an element from the queue DS

        Returns:
            Dequeued element
        """
        return self.items.remove_at_head()

    def length(self):
        """Get the length of the queue

        Returns:
            Length of the queue
        """
        return self.items.length

    def __str__(self):
        """Print the queue structure"""
        return self.items.__str__()
    pass
