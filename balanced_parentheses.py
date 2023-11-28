from DS.Stack.Stack import Stack


def is_balanced(exp: str) -> bool:
    my_stack = Stack()

    o = "([{"
    c = ")]}"
    for bracket in exp:
        if bracket in o:
            my_stack.push(bracket)
        else:
            popped = False
            for idx in range(len(c)):
                if bracket == c[idx] and my_stack.peek() == o[idx]:
                    my_stack.pop()
                    popped = True
                    break
            if popped is False:
                return False

    if my_stack.is_empty():
        return True
    return False


if __name__ == "__main__":
    print(is_balanced("[{(}]"))
    print(is_balanced("({[}]})"))
