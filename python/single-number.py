class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for number in nums:
            res = res ^ number
        
        
        return res
