import random
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    
    def encode(self, strs):
        #https://www.youtube.com/watch?v=B1k_sxOSgv8&ab_channel=NeetCode

        # We need to make sure that our encoding delimeter is not in the String
        # Because if we have # as a delimeter and our string is "vaquis vak#is"
        # encode vaquis#vak#is 
        # but when we decode we'll have:
        # vaquis vak is  
        res = ""
        for word in strs:
            res = res + str(len(word)) + '#' + word
        return res

        
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        print(str)
        res = []
        i = 0

        while i < len(str):
            
            j = i

            # get word length
            while str[j] != '#':
                j += 1
            length = int(str[i:j]) # we exit while loop once we reached our delimeter

            # get text and append from string
            start = j + 1
            end = j + length
            res.append(str[start : end + 1]) # + 1 cuz non inclusive

            i = end + 1 # move i to next 'word length' char

        return res
