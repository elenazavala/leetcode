class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        
        for key in nums:
            if key in table:
                table[key] += 1               
            else:
                table[key] = 1
            
            if table[key] > len(nums)/2:
                    return key
            
        # return None
            
            
        # for key in table:
        #     if table[key] > len(nums)/2:
        #         return key
        
             
        
