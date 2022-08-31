class Solution(object):
    def isAnagram(self, s, t):
        # for them to be anagrams they need to have
        # the same # of letters, and the same character count
         #if they are not the same length, return False immediately
            
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            charS, charT = s[i], t[i]
            sMap[charS] = 1 + sMap.get(charS, 0)
            tMap[charT] = 1 + tMap.get(charT, 0)
        
        if sMap == tMap:
            return True
        else:
            return False
