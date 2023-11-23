from DS.Queue.Queue import Queue
from DS.Stack.Stack import Stack

def reverse_first_k(queue: Queue, k: int) -> None:
    i = 0
    stack = Stack()

    while i < k:
        stack.push(queue.dequeue())
        i += 1

    while i >= 1:
        queue.enqueue(getattr(stack.pop(), "data"))
        i -= 1

    while queue.length() - k > 0:
        queue.enqueue(getattr(queue.dequeue(), "data"))
        k += 1


if __name__ == "__main__":
    queue = Queue()

    for num in range(1, 6):
        queue.enqueue(num)
    print(queue)

    reverse_first_k(queue, 4)
    print(queue)
