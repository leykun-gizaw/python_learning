from DS.Queue.Queue import Queue

def find_binary(number: int) -> list:
    """Provides list of strings of numbers from 1 to `number`

    It utilizes a queue to store the binary values. The sequence of which is
    very unique such that a dequeued node will give the next two binary numbers
    if appended '0' and '1' in that order. For example when 1 gets dequeued,
    adding '0' and '1' at the end gives '10' and '11'. The next dequeue will
    provide '10' on which appending '0' and '1' will provide 4 and 5,
    continuing from where it last stopped.

    Args:
        number (int): The upper limit

    Returns:
        List of binary number strings
    """
    x = []
    que = Queue()

    que.enqueue("1")

    for _ in range(1, number + 1):
        node = que.dequeue()

        x.append(node.data)

        que.enqueue(node.data + "0")
        que.enqueue(node.data + "1")

    return x
