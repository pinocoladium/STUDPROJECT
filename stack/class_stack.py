class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        last = self.stack.pop(-1)
        return last

    def peek(self):
        last = self.stack[-1]
        return last

    def size(self):
        len_stack = len(self.stack)
        return len_stack
