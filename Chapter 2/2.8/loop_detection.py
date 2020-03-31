#Given a circular linked list, return node at the beginning of the loop

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def loop_detection(node):
    fast = node
    slow = node
    while fast and fast.next and slow:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: #if there is a loop, this means that slow and fast will eventually intersect 
            break
        if slow == None and fast == None: #if there isn't a loop, both slow and fast will be None
            return None
    slow = node #set slow back to the start of the node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.value

# A > B > C > D > E > C
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

loop_detection(a)
#output: C
