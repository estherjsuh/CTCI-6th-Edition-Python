#Delete Middle Node - any node but first and last of singly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.next != None:
            lastnode = lastnode.next
        lastnode.next = newnode
    def printList(self):
        head = self.head
        while head:
            print(head.value)
            head = head.next
    def deleteMidNode(self, delnode): #not first or last
        currnode = self.head
        prevnode = None
        while currnode.value != delnode:
            prevnode = currnode
            currnode = currnode.next
        prevnode.next = currnode.next
        currnode = None
        
 
ll = LinkedList()

ll.append('A')
ll.append('B')
ll.append('C')
ll.append('D')
ll.printList()

ll.deleteNode('C')
ll.printList()

ll.deleteNode('B')
ll.printList()

