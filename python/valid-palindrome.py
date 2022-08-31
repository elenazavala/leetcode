class Solution(object):
    def isPalindrome(self, s):
    
        # create a temp string skipping all non alphanumeric characters
        temp = ""
        for char in s:
            if char.isalnum():
                temp = temp + char 
        temp = temp.lower()
        print(temp)
        #now we will have one huge word: temp
        
        l = 0
        r = len(temp) - 1
        
        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
            
        return True
