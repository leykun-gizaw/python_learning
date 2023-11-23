class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
        return

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def pop(self):
        if self.is_empty() is not True:
            self.stack_size -= 1
            return self.stack_list.pop()
        return None
