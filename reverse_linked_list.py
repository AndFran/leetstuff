from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        # we swap the next with what was previous
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev  # new head


def printList(node: ListNode):
    prev = None
    curr = node
    while curr:
        # go through and keep track of prev
        print("prev is", prev.val if prev else "None")
        print("val", curr.val)
        prev = curr
        curr = curr.next


four = ListNode(4, None)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
head = ListNode(0, one)
head = reverseList(head)
printList(head)



