class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        
        nums.sort()
        
        
        self.dfs(nums, path, result)
        
        return result
    
    
    def dfs(self, nums, path, result):
        
        result.append(path)
        
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                self.dfs(nums[i+1:], path + [nums[i]], result)
