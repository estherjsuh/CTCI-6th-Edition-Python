#Stack of Plates using list of lists

class StackofPlates:
    def __init__(self):
        self.sets = []
        self.substack = 0
    def push(self, value):
        if self.sets == []:
            self.sets.append([value])
        else:
            if len(self.sets[self.substack]) < 5: #when stack is full
                self.sets[self.substack].append(value)
            else:
                self.sets.append([value])
                self.substack += 1
    def size(self):
        return self.substack + 1
    def pop(self):
        if len(self.sets[self.substack]) == 0:
            self.substack -= 1
        return self.sets[self.substack].pop()
    def popAt(self, substack_ind):
        if substack_ind > self.substack:
            return "out of range"
        else:
            return self.leftShift(substack_ind) 
        #self.sets[substack_ind].pop()
    def leftShift(self, substack_ind):
        remove = self.sets[substack_ind].pop()
        if substack_ind < self.substack:
            self.sets[substack_ind].append(self.sets[self.substack].pop())
        return remove
    def peek(self, substack_ind):
        return self.sets[substack_ind][-1]
        
        
