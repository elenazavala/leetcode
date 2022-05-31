class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        
        if (n == 0):
            return t0
        
        for i in range(3, n+1):
            nextT =  t0 + t1 + t2 
            t0 = t1
            t1 = t2
            t2 = nextT
            
        return t2
        
