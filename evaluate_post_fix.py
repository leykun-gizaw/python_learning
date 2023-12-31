from DS.Stack.Stack import Stack

def evaluate_post_fix(exp: str):
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
                stack.push(int(evaluate(second, first, op[1])))
                break
        if op_found is False:
            stack.push(int(char))

    return stack.pop()

def evaluate(x: int or float, y: int or float, operator: str) -> int or float:
    res = getattr(x, operator)(y)
    return getattr(x, operator)(y)

def evaluate_post_fix2(exp: str):
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
    except:
        return "Invalid Sequence"


if __name__ == "__main__":
    print(evaluate_post_fix2("921*-8-4+"))
    print()
    print(evaluate_post_fix2("642/+"))
