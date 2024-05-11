from DS.Stack.Stack import Stack


def is_balanced(exp: str) -> bool:
    """Function is responsible for checking parentheses balance

    **This function uses lists to represent supported parentheses types (both opening and closing). Usage of better
    data types like sets or dictionaries for lookup is also possible but not really required. That is b/c for any
    size of `exp` the biggest range that can be traversed in search of a closing parenthesis is only 3.**

    *Complexity analysis:*
        *Time: O(n)
            *Explanation:*
                *For any size of `exp` (n), we have two inner loops, both that can traverse 3 times in the worst case.*
                *From the inner loops only one will run at a time. So 3*n will be the total time in the worst case.*

        *Space: O(n)*
            *Explanation:*
                *In the worst case, the stack will be the same size as `exp`.*

    Args:
        exp: String to inspect

    Returns:
        True if all parentheses are balanced, False otherwise

    """
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
    print(is_balanced("[]"))
    print(is_balanced("({[}]})"))
