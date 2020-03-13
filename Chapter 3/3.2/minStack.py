#Stack min - design a stack that push/pop/returns min @ 0(1)

class Stack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []
        
    def push(self, value):
        self.mainStack.append(value)
        
        if self.minStack == []:
            self.minStack.append(value)
        elif value <= self.minStack[-1]:
                self.minStack.append(value)
        
    def pop(self):
        value = self.mainStack.pop()
        
        if value == self.minStack[-1]:
            self.minStack.pop()
                    
    def returnMin(self):
        return self.minStack[-1]
        
    def printStack(self):
        if self.mainStack == []:
            return
        for i in self.mainStack[::-1]:
            print(i)
