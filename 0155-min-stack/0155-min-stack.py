class MinStack:

    def __init__(self):
        self.stack = []
        self.s = []
    
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
        else:
            self.stack.append(min(value, self.stack[-1]))
        self.s.append(value)

    def pop(self) -> None:
        self.s.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()