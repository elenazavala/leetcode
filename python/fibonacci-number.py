class Solution:
    def fib(self, n: int) -> int:
        firstFib = 0
        secondFib = 1
        
        if n == 0:
            return firstFib

        
        for i in range(2, n+1):
            nextFib = firstFib + secondFib
            
            firstFib = secondFib
            secondFib = nextFib
            
        return secondFib
            
