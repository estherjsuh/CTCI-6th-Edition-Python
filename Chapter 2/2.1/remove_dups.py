#Remove Duplicates from Linked List

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
        currNode = self.head
        while currNode:
            print(currNode.value)
            currNode = currNode.next
            
    def removeDups(self):
        currNode = self.head
        prevNode = None
        hash = {}
        while currNode:
            if currNode.value in hash:
                prevNode.next = currNode.next
                currNode = None
            else:
                hash[currNode.value] = 1
                prevNode = currNode
            currNode = prevNode.next
    
    
ll = LinkedList()
ll.append('A')
ll.append('B')
ll.append('Z')
ll.append('A')
ll.append('B')

ll.printList()

ll.removeDups()

ll.printList()
