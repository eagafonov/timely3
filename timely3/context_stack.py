class context_stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0

    def len(self):
        return len(self.stack)

    def items(self):
        yield from self.stack

    def ritems(self):
        yield from reversed(self.stack)
