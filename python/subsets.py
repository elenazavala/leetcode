class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
  

        def dfs(nums, path):
            result.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])
            
