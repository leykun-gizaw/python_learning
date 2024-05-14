# Create a new list with highest elements seen from the right
#
#   Eg. for a list lst = [10, 5, 2, 13, 15, 9, 2, 16]
#   the newly created list will be [13, 13, 13, 15, 16, 16, 16, -1]
#
#   Elements in the new list will be replacements of elements in the same index of the original list. Only this time
#   they will hold values of the first encountered highest element when traversing to the right.

from DS.Stack.Stack import Stack


def next_greater_element1(lst: list) -> list:
    """Get the result using bruteforce approach

    Complexity analysis:
        Time: O(n^2) b/c the actual number of cycles is n(n+1)/2
        Space: O(n)

    Args:
        lst: List to analyze

    Returns:
        Next greater elements list
    """
    result = list()

    for i in range(len(lst)):
        next_greatest = -1
        for j in range(i, len(lst)):
            if lst[j] > lst[i]:
                next_greatest = lst[j]
                break
        result.append(next_greatest)

    return result


def next_greater_element2(lst: list) -> list:
    """Use a decreasing monotonic stack to reduce time by using some space

    Complexity analysis:
        Time: O(n) b/c in the worst case the stack will store n - 1 elements that get poped at once.
        Space: O(n) b/c in any case we create a new list with the exact size.

    Args:
        lst: List to analyze

    Returns:
        Next greater elements list
        """
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


def next_greater_element3(lst: list) -> list:
    """Use stack but start from the beginning

    Complexity analysis: Similary to above

    Args:
        lst: List to analyze

    Returns:
        Next greater elements list
    """

    stack = Stack()
    result = [-1] * len(lst)

    for idx in range(len(lst)):
        while stack.is_empty() is False and stack.peek()[1] < lst[idx]:
            val = stack.pop()
            result[val[0]] = lst[idx]
        stack.push([idx, lst[idx]])

    return result


if __name__ == "__main__":
    nums1 = [4, 6, 3, 2, 8, 1]

    print(next_greater_element1(nums1))
    print(next_greater_element2(nums1))
    print(next_greater_element3(nums1))
