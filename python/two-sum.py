class Solution(object):
    def twoSum(self, nums, target):
        
        mappy = {}
        for i in range(len(nums)):
            diff = target - nums[i] #ver si hay este numero "diff" en el mapa. Si hay, encontramos el two sum
            if diff in mappy:
                return mappy[diff], i #retornar index del current number y de diff
            else:
                mappy[nums[i]] = i  # aca mappeamos el index con el numero en el q estamos
        
