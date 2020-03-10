#Queue via Stacks - implement queue using 2 stacks

class MyQueue:
    def __init__(self):
        self.instack = []
        self.outstack = []
        
    def enqueue(self, value):
        self.instack.append(value)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
  
  
