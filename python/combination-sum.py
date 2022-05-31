class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        
        def dfs(candidates, path, target):
            if target == 0:
                result.append(path)
                return 
            
            if target < 0:
                return 
            
            for i in range(len(candidates)):
                dfs(candidates[i:], path + [candidates[i]], target - candidates[i])
            
        dfs(candidates, path, target)
        
        return result
