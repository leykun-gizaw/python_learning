class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
        self.max_elem_length = 0
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
        if self.max_elem_length < len(str(value)):
            self.max_elem_length = len(str(value))

    def pop(self):
        if self.is_empty() is not True:
            self.stack_size -= 1
            return self.stack_list.pop()
        self.max_elem_length = max(len(str(elem)) for elem in self.stack_list)
        return None

    def __str__(self):
        val = ""
        for elem in reversed(self.stack_list):
            print("|", str(elem).center(self.max_elem_length), "|")
        return val
