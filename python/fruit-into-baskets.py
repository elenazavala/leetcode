class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        # What is the length of longest subarray that contains up to two distinct integers?
        
        left = 0
        maximumSize = 0
        lengthOfDistinct = 0
        fruits = {}
        
        for fruit in tree:
            if fruit not in fruits:
                fruits[fruit] = 0

        
        
        for right in range(len(tree)):
            if  fruits[tree[right]] == 0:
                lengthOfDistinct += 1 
               
            
            fruits[tree[right]] += 1 
               
            
            while lengthOfDistinct > 2 and left < len(tree):                
                fruits[tree[left]] -= 1
                if fruits[tree[left]] == 0:
                    lengthOfDistinct -= 1
                
                left += 1
            
            currentSize = right - left + 1
            maximumSize = max(currentSize, maximumSize)
            
            
        return maximumSize
    

#   [3,3,3,1,2,1,1,2,3,3,4]


# { 3: 3, 1: 1}

# size = 
