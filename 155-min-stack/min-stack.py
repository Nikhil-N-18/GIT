class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, value: int) -> None:
        self.stack1.append(value)
        if not self.stack2:
            self.stack2.append(value)
        else:
            self.stack2.append(min(value,self.stack2[-1]))
    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()        
    def top(self) -> int:
        return self.stack1[-1]
    def getMin(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()