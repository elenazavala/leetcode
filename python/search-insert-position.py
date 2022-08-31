class Solution(object):
    def searchInsert(self, nums, target):
       # hice a mano aca https://docs.google.com/document/d/1HFDqjDMSaRYSDHtFG7bNVDOFc2olyzJx6GxYOYldHCI/edit
        left = 0
        right = len(nums) - 1
        
        # if current number is larger than target
        # right = mid - 1
        
        # if current number is smaller than target
        # left = left + 1
        
        while left <= right:
            mid = right + left // 2 # take the average
            print("Mid is", + mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        
        return left  #cuando hacemos esto manualmente me dare cuenta que siempre left termina siendo el value donde deberiamos poner el numero a insertar
    
        #if we continue with the whole array we'll see that wherever
        # our left pointer ends up is where we would put the target
        
