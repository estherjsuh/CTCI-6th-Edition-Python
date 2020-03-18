#Partition a linked list around a value x; nodes < x to left, nodes >= x to right

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        currnode = self.head
        if self.head == None:
            self.head = Node(value)
            return
        while currnode.next != None:
            currnode = currnode.next
        newnode = Node(value)
        currnode.next = newnode
        
    def printList(self):
        head = self.head
        string = ""
        while head:
            pll += str(head.value)+ ' -> '
            head = head.next
        return string
        
ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)
ll.printList()
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 ->
        
        
#create 2 linked list; first LL with nodes < x, second LL with nodes >= x   
#then add the nodes from second LL to first LL
 
def partition(ll, n):
   first = LinkedList()
   second = LinkedList()
   curr = ll.head
   while curr:
       if curr.value < n:
           first.append(curr.value)
       else:
           second.append(curr.value)
       curr = curr.next
   
   secnode= second.head
   while secnode:
       first.append(secnode.value)
       sechead = secnode.next
    
   return first.printList()


partition(ll, 5)
# 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10 ->

        
        
