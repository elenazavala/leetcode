class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #       1  2  3  4
        # Pre:  1  2  6  4 
        # Post: 24 24 12 4
        # Output: [1: Pre*Post , 2: Pre*Post, 3: Pre*Post ...]
        # Output : [24, 12, 8, 6]
        # * for first and last indeces, since there is nothing before/after, we just multiply by 1
        
        #First we calculate the prefix and store that in the output
        #Then, we calculate the postfix and multipliy that with whatever is in the output
        
        ## alfinal eso no hice ^^^^^ hice de la forma para tontis,calculando prefix y postfix aparte
        # y luego manejando edgecases para el primer y ultimo numero del array
        
        pre, post, result = [], [] , []
        prefix,postfix = 1, 1

        for i in range(len(nums)):
            prefix = prefix * nums[i]
            pre.append(prefix)
            
        for i in reversed(range(len(nums))):
            postfix = postfix * nums[i]
            post.append(postfix)
        post.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                result.append(1 * post[i+1])
            elif i == len(nums) - 1:
                result.append(pre[i-1] * 1)
            else:
                result.append(pre[i-1] * post[i+1])
                
        return(result)
