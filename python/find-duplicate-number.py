class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        FIRST SOLUTION: Sort. (Does not satisfy conditions, see last submition for one that satisfies)
        We are going to use a left and right pointer,
        left starts at index 0 and right at 1.
        Next we compare the two values at those positions,
        if they are not the same advance each 1 spot.
        
        We are going to repeat this until the right pointer
        reached the last element on the list
        
        Note: This approach modifies individual elements and does not use constant space, and hence does not         meet the problem constraints. However, it utilizes a fundamental concept that can help solve                 similar problems.

        Intuition

        In an unsorted array, duplicate elements may be scattered across the array. However, in a sorted             array, duplicate numbers will be next to each other.
        '''
        nums.sort() # I believe this is O(1) space as sorting happens in place, worst case O(n)
        left, right = 0, 1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
            right += 1
            left += 1
        
        # another sol, we start from 1 and compare to the previous
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
