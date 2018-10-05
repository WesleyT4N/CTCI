def sort_stack(stack):
    primary = stack
    secondary = Stack()
    if stack.is_empty():
        return stack
    while not primary.is_empty():
        curr = primary.pop()
        while not secondary.is_empty() and secondary.peek() > curr:
            primary.push(secondary.pop())
        secondary.push(curr)
    while not secondary.is_empty():
        primary.push(secondary.pop())
    
    return primary