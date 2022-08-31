class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        # A number will be the START of a sequence if
        # it doesn't have a left neighbor..
        
        # So in our set, we wil check if a number is the start of a
        # sequence, then try to make it as long as we can
    
        
        numSet = set(nums) #useful syntax, avoid populating with a loop
        longest, length = 0, 0 #length is used as a counter to keep checking for consecutive numbers
        
        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in numSet: 
                length = 0
                while(n + length) in numSet: 
                    length += 1
                
                longest = max(longest,length)
        
        return longest
        
        # code walkthrough
        # What's happenin after the if statement?
        #
        # say now we are at 1, where n = 1 
        # in the while loop, where length starts at 0
        # n + 0  >>> 1 + 0 in numSet
        # length = 1
        # 
        # n + 1 >>> 1 + 1  in numset
        # length = 2
        #
        # n + 2 >>> 1 + 2 in numset
        # length = 3
        # 
        # n + 3 >>> 1 + 3 in numset
        # length = 4
        #
        # n + 4 >>> 1 + 4 in numset
        # BREAK LOOP
