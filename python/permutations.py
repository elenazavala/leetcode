class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = []
        
        self.DFS(nums, permutations, result)
        
        return result
    
    
    def DFS(self, nums, currentPermutation, result):
        if len(nums) == 0:
            result.append(currentPermutation)
            
        else:
            for i in range(len(nums)):
                newArray = nums[:i] + nums[i+1:]
                newPermutation = currentPermutation + [nums[i]]
                self.DFS(newArray, newPermutation, result)     
