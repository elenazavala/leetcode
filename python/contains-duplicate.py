class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        mappy = {}
        
        for num in nums:
            if num in mappy:
                return True
            else:
                mappy[num] = 1
        
        return False
