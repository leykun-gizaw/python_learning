from DS.Stack.Stack import Stack


def sort_stack(stack: Stack) -> Stack:
    helper = Stack()

    while stack.is_empty() is False:
        top = stack.pop()

        if helper.is_empty() or helper.peek() <= top:
            helper.push(top)
        else:
            while helper.is_empty() is False:
                stack.push(helper.pop())
            stack.push(top)

    return helper


if __name__ == "__main__":
    stack = Stack()
    nums = [23, 60, 12, 42, 4, 97, 2]

    for num in nums:
        stack.push(num)

    print(stack)
    sorted = sort_stack(stack)
    print(sorted)
