class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = {0:0, 1:0}
        
        longestSubarray = 0
        
        left = 0
        
        for right in range(len(A)):
            count[A[right]] += 1
            
            while count[0] > K and left < len(A):
                count[A[left]] -= 1
                left += 1
                
            currentLongest = right - left + 1
                

            longestSubarray = max(longestSubarray, currentLongest)
            
            
        return longestSubarray
