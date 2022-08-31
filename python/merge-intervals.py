class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        0----2          1----3
           1 --- 4         2----6
              3-----5             8----10
                                         15----18
        First we are going to sort the intervals by the smallest START vals
        
        Then create a res = [] and append the first interval
        
        Now we gonna keep comparing the current interval to the last
        interval we added in our result list. If the current first element
        is smaller than the last.element.added's END.. then they are
        overlapping and take the biggest END from both and make it our new
        result's last elem added end's
        
        If they do not overlap we still append it to our list
        
        Syntax Notes
        1. We are going to use lambda shit to make sure we sort the first 
           element [THIS, THISNOT] so [1,3] [8,10] we make sure we are sorting 
           the 1 and 8
        
        2. We use listname[-1] to get the most recent element added to the list.
           Now.. [1,2] start '1' is at 0 pos and end '2' is at 1
           So here we use output[-1][1] since the END is at that position and
           this is what we need to look into to see if intervals overlap
           when comparing
        
        3. In our for loop we use intervals [1:].. this is a slice notation, 
           so we can skip first the element 0 and start at 1 since we already added
           the first element
        '''
        #O(nlogn)
        
        intervals.sort(key = lambda i:i[0]) 
        res = [intervals[0]] #insert something there to avoid edge case
        
        for start, end in intervals[1:]: 
            last_end = res[-1][1] #last intervaladded's end
            
            if start <= last_end:
                #update end value, no need to update start as it will already be the smallest
                biggestEnd = max(end, last_end)
                res[-1][1] = biggestEnd
            else:
                #they do not overlap but we still need to add them to our output
                res.append([start, end])
            
        return res
