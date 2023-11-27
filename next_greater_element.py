from DS.Stack.Stack import Stack


def next_greater_element(lst: list) -> list:
    my_stack = Stack()
    result = [-1] * len(lst)

    for idx in range(len(lst) - 1, -1, -1):
        if my_stack.is_empty():
            my_stack.push(lst[idx])
            continue

        while my_stack.is_empty() is False:
            if my_stack.peek() > lst[idx]:
                result[idx] = my_stack.peek()
                my_stack.push(lst[idx])
                break
            my_stack.pop()

        my_stack.push(lst[idx])
        
    return result


if __name__ == "__main__":
    def test(lst):
        print(lst)
        result = next_greater_element(lst)
        print(result)

    lst1 = [4, 6, 3, 2, 8, 1]
    lst2 = [4, 6, 3, 2, 8, 1, 9, 9, 9]

    test(lst1)
    test(lst2)
