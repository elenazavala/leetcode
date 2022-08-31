class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        currentPermutation = []
        
        self.DFS(nums, currentPermutation, result)        
        return result
    
    def DFS(self, nums, currentPermutation, result):
        if len(nums) == 0:
            if currentPermutation not in result:
                result.append(currentPermutation)
                
        else:
            for i in range(len(nums)):
                newArray = nums[:i] + nums[i+1:]
                newPermutation = currentPermutation + [nums[i]]
                self.DFS(newArray, newPermutation, result)
