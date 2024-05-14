from DS.Stack.Stack import Stack


def evaluate_post_fix(exp: str):
    """Evaluate post-fix calculations

    This function uses a hard-coded operators along with built-in methods that represent them.
    The algorithm works by first going through `exp` and for each character it finds, it tries to search its
    corresponding method. Once found, it evaluates the proper expression and pushes it back to the stack.

    Complexity analysis:
        Time: O(n)
            *Explanation: For any size of `exp` the inner loop in the worst case loops only 5 times.*
        Space: O(n)
            *Explanation: In the worst case we only have digits in `exp`.

    Args:
        exp: Post-fix string to evaluate

    Returns:
        Result of operation
    """
    stack = Stack()
    operators = [
        ["+", "__add__"],
        ["-", "__sub__"],
        ["*", "__mul__"],
        ["/", "__truediv__"],
        ["%", "__mod__"]
    ]

    for char in exp:
        op_found = False
        for op in operators:
            if char == op[0]:
                op_found = True
                first = stack.pop()
                second = stack.pop()
                try:
                    stack.push(int(evaluate(second, first, op[1])))
                except AttributeError:
                    return "Invalid Sequence"
                break
        if op_found is False:
            stack.push(int(char))

    return stack.pop()


def evaluate(x: int or float, y: int or float, operator: str) -> int or float:
    return getattr(x, operator)(y)


def evaluate_post_fix2(exp: str):
    """Evaluate post-fix calculations using `eval`

    This function uses `eval` instead of going through a custom list of functions to use.

    Complexity analysis:
        Time: O(n)
            Explanation: In any case it is important to go through the whole string.
        Space: O(n)
            Explanation: In the worst case we only have digits in `exp`. So the stack size will roughly be the same
            as number of digits in `exp`.

    Args:
        exp: Post-fix string to evaluate

    Returns:
        Result of operation
    """
    stack = Stack()

    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                first = stack.pop()
                second = stack.pop()

                stack.push(str(eval(second + char + first)))
        return stack.pop()
    except TypeError:
        return "Invalid Sequence"


if __name__ == "__main__":
    print(evaluate_post_fix2("921*-8-4+"))
    print()
    print(evaluate_post_fix2("642/+"))
    print(evaluate_post_fix2("62/+"))
