class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        map = {}
        nums.append(nums[0])
        
        for i in range(len(nums)):
            map[i] = i
        
        for i in range(len(nums)):
            if nums[i] in map:
                map.pop(nums[i])
        
        for key in map.keys():
             return(key)

