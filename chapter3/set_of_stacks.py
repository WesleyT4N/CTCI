class fixedSizeStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.free = 0
        self.size = size
    
    def push(self, data):
        if self.free < self.size:
            self.stack[self.free] = data
            self.free += 1
    
    def pop(self):
        if self.free >= 0:
            tmp = self.stack[self.free]
            self.stack[self.free] = None
            self.free -= 1
            return tmp

    def has_space(self):
        self.free < self.size
    
    def is_empty(self):
        self.free == 0

class SetOfStacks:

    def __init__(self, capacity):
        self.set = [fixedSizeStack(capacity)]
        self.free = 0
        self.capacity = capacity

    def push(self, data):
        stack = self.set[self.free]
        if not stack.has_space:
            self.set.append(fixedSizeStack(self.capacity))
            self.free += 1
            stack = self.set[self.free]
        stack.push(data)
    
    def pop(self, data):
        stack = self.set[self.free]
        if stack.is_empty():
            self.set.pop()
            self.free -= 1
            stack = self.set[self.free]
        return stack.pop()

    def popAt(self, index):
        if index > self.free:
            return None
        stack = self.set[index]
        if stack.is_empty:
            return None
        return stack.pop()