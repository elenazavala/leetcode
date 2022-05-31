class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Same concept as two sum II, binary search sort of, 
        # but with a fixed value
        res = []
        nums.sort()
        
        
        #outer loop keep tright of current/fixed number
        #inner loop manages the left and right pointer
        for i, fixed in enumerate(nums):
            if i > 0  and fixed == nums[i-1]:    #avoid duplicates as fixed values, if its not the first value, and the next value is same as prior val 
                continue                         #continue to next iteration of the loop
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = fixed + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([fixed, nums[l], nums[r]])
                    # [-2, -2, 0, 0, 2, 2]
                    #  l                r  what if our pointers were here and we found a solution for an 'A'  fixed value
                    l += 1 #we shift left as there could be more combinations with this fixed number, so we continue until we test everything until l < r
                    while nums[l] == nums[l - 1] and l < r: #avoiding duplicates
                        l += 1
                        
        return res
