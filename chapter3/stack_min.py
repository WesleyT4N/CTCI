
class StackWithMin:

    class StackNode:
        def __init__(self, data=None):
            self.data = data
            self.next = None


    def __init__(self):
        self.top = None
        self.minStack = []

    def min(self):
        return self.minStack[-1]

    def push(self, data):
        if self.top:
            new_top = self.StackNode(data)
            new_top.next = self.top
            if (data <= self.min()):
                self.minStack.append(data)
            self.top = new_top
        else:
            self.top = self.StackNode(data)
            self.minStack.append(data)
    
    def peek(self):
        return self.top.data
    
    def pop(self):
        if self.top is None:
            raise EmptyStackException()
        else:
            value = self.top
            if (self.min() == self.top.data):
                self.minStack.pop()
            self.top = self.top.next
            return value

    def min(self):
        if self.top is None:
            raise EmptyStackException()
        else:
            return self.top.min_below
        
