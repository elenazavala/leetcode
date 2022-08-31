class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if index is less than denomination skip it
        ways = [float("inf") for _ in range(amount + 1)]
        
        ways[0] = 0
        
       
        for coin in coins:
            for amount in range(1,len(ways)):
                if coin <= amount:
                    coinsNeeded = amount - coin                
                    ways[amount] = min(ways[amount], ways[coinsNeeded] + 1)
        
        
        
        return ways[amount] if ways[amount] != float("inf") else -1
        
