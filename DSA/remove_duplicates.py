from LinkedList import SLList

def remove_duplicates(llist: SLList.SLList):
    current = llist.get_head()

    while current is not None:
        next = current.next
        prev = current
        while next is not None:
            temp = None
            if next.data == current.data:
                prev.next = next.next
                temp = next
            else:
                prev = next
            next = next.next
            if temp is not None:
                temp.next = None

        current = current.next
    return

def remove_duplicates2(llist: SLList.SLList):
    """Use a data structure to store duplicates
    """

    if llist.is_empty():
        return

    prev = llist.get_head()
    cur = prev.next
    duplicates = [prev]

    while cur is not None:
        dup_found = False
        for dup in duplicates:
            if dup.data == cur.data:
                prev.next = cur.next
                dup_found = True
                break

        if dup_found is False:
            duplicates.append(cur)
            prev = cur
        cur = cur.next


def remove_duplicates3(llist: SLList.SLList):
    n = llist.get_head()
    m = None

    while n is not None:
        m = n.next
        prev = n
        while m is not None:
            if n.data == m.data:
                prev.next = m.next
                break
            prev = m
            m = m.next
        n = n.next


if __name__ == "__main__":
    llist = SLList.SLList()

    for num in range(5):
        if num % 2 == 0:
            llist.insert_at_head(num)
            llist.insert_at_head(num)
        llist.insert_at_head(num)

    print(llist)
    print()

    remove_duplicates2(llist)

    print(llist)
