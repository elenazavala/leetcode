class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      
        
        totalLength = len(nums1) + len(nums2)
        
        index1 = 0
        index2 = 0
        mergeArray = []
        
        while index1 < len(nums1) or index2 < len(nums2):
            if index1 <  len(nums1):
                val1 = nums1[index1]
            else:
                val1 = float("inf")

                
            if index2 < len(nums2):
                val2 = nums2[index2]

            else:
                val2 = float("inf")   
                
            if val1 <= val2:
                mergeArray.append(val1)
                index1 += 1
            else:
                mergeArray.append(val2)
                index2 += 1
                
        if totalLength % 2 == 1:
            return mergeArray[totalLength//2]
        
        
        return (mergeArray[totalLength//2] + mergeArray[totalLength//2 - 1])/2
