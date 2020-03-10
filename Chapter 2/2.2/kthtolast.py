#Kth to Last element of single linked list

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
            
    def kthtolast(self,k):
        size = 0
        currnode = self.head
        while currnode:
            size+=1
            currnode = currnode.next
            
        if k > size:
            raise IndexError("Out of range")
            return
        
        count = 0
        target = size - k
        targetnode = self.head
        while count != target and targetnode:
            targetnode = targetnode.next
            count += 1
        
        return targetnode.value
