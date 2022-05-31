class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        result = []
        path = []
        
        def dfs(candidates, path, target):
            if target == 0:
                result.append(path)
                return 
            if target < 0:
                return
            
            
            for i in range(len(candidates)):
                if i == 0 or candidates[i-1] != candidates[i]:
                    dfs(candidates[i+1:], path + [candidates[i]], target - candidates[i])
        
        
        
        
        dfs(candidates, path, target)
            
        
        return result
