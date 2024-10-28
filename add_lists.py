"""
Compute 712 + 173 normally. The sum is 885:

   712
 + 173
 -----
   885

    7 -> 1 -> 2
 +  1 -> 7 -> 3
 --------------
    8 -> 8 -> 5

Notice we get the linked list back also in reversed format

"""


class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return str(self)


def show(node: Node):
    print("showing all")
    current = node
    while current:
        print(current.val)
        current = current.next


def add_lists(list1: Node, list2: Node):
    current1 = list1
    current2 = list2
    dummy_head = Node(0)
    tail = dummy_head
    carry = 0

    while current1:
        if current2 is None:
            current2_val = 0
        else:
            current2_val = current2.val

        result = current1.val + current2_val + carry
        if carry > 0:
            carry = 0
        if result > 9:
            result = result - 10
            carry = 1

        tail.next = Node(result)

        current1 = current1.next

        if current2 is not None:
            current2 = current2.next
        tail = tail.next

    if carry > 0:
        tail.next = Node(carry)

    return dummy_head.next



a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)

res = add_lists(a1, b1)
show(res)
