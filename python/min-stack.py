class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")
        
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = min(x, self.min)
        

    def pop(self) -> None:
        if self.min == self.stack.pop(-1):
            self.min = float("inf")
            for i in range(len(self.stack)):                
                self.min = min(self.min, self.stack[i])
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
