from DS.LinkedList.SLList import SLList

def remove_duplicates1(llist: SLList):
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


def remove_duplicates2(llist: SLList):
    """Use only O(1) space"""
    n = llist.get_head()
    m = None

    while n is not None:
        removed = None
        m = n.next
        prev = n
        while m is not None:
            if n.data == m.data:
                prev.next = m.next
            else:
                prev = m
            m = m.next

            if removed is not None:
                removed.next = None
        n = n.next


if __name__ == "__main__":
    llist = SLList()

    for num in range(8):
        if num % 2 == 0:
            llist.insert_at_head(num)
            llist.insert_at_head(num)
        llist.insert_at_head(num)

    print(llist)
    print()

    remove_duplicates2(llist)

    print(llist)
