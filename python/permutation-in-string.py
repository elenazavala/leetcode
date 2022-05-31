class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ''' 
        Sliding Window Solution.
        We create two hashmaps, we initially fill one with s1 count of specific chars.
        Next we create a window of the size of s1, 
        
        Start that window on the beginning of the s2 and test all possible
        windows of size s1 from the start of s2 to the end.. to look 
        for a single permutation.
        
        We fill the map2 in each window to compare with map1
        '''
        if len(s1) > len(s2):
            return False
        
        map_s1, map_s2 = {}, {}
        
        for char in s1:
            map_s1[char] = 1 + map_s1.get(char, 0)
        
        #sliding window
        l = 0
        r = len(s1) - 1 # note 1
        
        while r < len(s2): # note 2
            for i in range(l, r+1): # note 3
                map_s2[s2[i]] = 1 + map_s2.get(s2[i], 0)
            if map_s1 == map_s2:
                return True
            else:
                map_s2.clear()
                
            l += 1 # advance window beginning
            r += 1 # advance window end
        
        # Index of Notex
        # Note 1: 
        # Our window will be the size of the string s1.
        # So left and right pointers mark the beginning and end of our window.
        # s1 = ab -> window length = 2
        
        # Note 2:
        # Eventually, our right pointer will arrive at the last character of our string,
        # so we want to traverse the whole string to test all possible strings
        # of the size of our window
        
        # Note 3:
        # This is where we populate our map2 according to our window beginning and end pointers
        # Note that the r+1 is cuz its non inclusive
