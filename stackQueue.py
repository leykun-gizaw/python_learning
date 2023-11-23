from  DS.Stack.Stack import Stack

class newQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.helper_stack = Stack()
        pass

    def is_empty(self):
        if self.main_stack.is_empty() and self.helper_stack.is_empty():
            return True
        return False

    def enqueue(self, value):
        self.main_stack.push(value)
        pass

    def dequeue(self):
        if self.helper_stack.is_empty():
            while self.main_stack.is_empty() is False:
                self.helper_stack.push(self.main_stack.pop())

        return self.helper_stack.pop()
    pass


if __name__ == "__main__":
    queue = newQueue()

    for i in range(5):
        queue.enqueue(i+1)
    for i in range(3):
        print(queue.dequeue(), end=" ")
    print()

    for i in range(6, 16):
        queue.enqueue(i)
    while queue.is_empty() is False:
        print(queue.dequeue(), end=" ")
    print()
