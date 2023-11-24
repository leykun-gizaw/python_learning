from DS.Stack.Stack import Stack


def sort_stack(stack: Stack, descending=False) -> None:
    """Function sorts a stack. It is a mutating function

    `stack` (Stack): The stack to sort
    `descending` (bool): Order of sort

    Returns:
        None
    """
    helper = Stack()

    while stack.is_empty() is False:
        top = stack.pop()

        if helper.is_empty() or helper.peek() <= top:
            helper.push(top)
        else:
            while helper.is_empty() is False:
                stack.push(helper.pop())
            stack.push(top)

    if descending is True:
        helper2 = Stack()
        while helper.is_empty() is False:
            helper2.push(helper.pop())
        while helper2.is_empty() is False:
            stack.push(helper2.pop())
        pass
    else:
        while helper.is_empty() is False:
            stack.push(helper.pop())


if __name__ == "__main__":
    stack = Stack()
    nums = [23, 60, 12, 42, 4, 97, 2]

    for num in nums:
        stack.push(num)

    print(stack)
    sort_stack(stack)
    print(stack)
    sort_stack(stack, descending=True)
    print(stack)
