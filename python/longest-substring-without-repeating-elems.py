class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     
        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in seen: #move left pointer 1 after the repeater character
                seen.remove(s[left]) #remove leftmost
                left += 1 #slide window
                
            window_length = right - left + 1
            res = max(window_length, res)
            seen.add(s[right])

        return res
