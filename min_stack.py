from DS.Stack.Stack import Stack
from random import random


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minimums = Stack()
        return

    def pop(self):
        if self.peek() == self.minimums.peek():
            self.minimums.pop()
        return super().pop()

    def push(self, value):
        if self.minimums.is_empty() or value < self.minimums.peek():
            self.minimums.push(value)

        super().push(value)

    def min(self):
        return self.minimums.peek()
    pass


if __name__ == "__main__":
    stack = MinStack()

    lst = [round(random() * 10) for _ in range(10)]
    
    for elem in lst:
        stack.push(elem)

    print(stack)
    print(stack.minimums)
    print(stack.min())
