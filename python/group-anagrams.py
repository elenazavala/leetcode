class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a map where the key is the sorted word,
        # and values are all words that are anagram to that
        # we check if the word is an anagram to the key by
        # simply sorting it too and see if its in the map **hack**
        
        mymap = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in mymap:
                mymap[sorted_word].append(word)
            else:
                mymap[sorted_word] = [word] #populate map and already add that word
        
        # mymap output should be..
        #{'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        # so we need to return the map values
        
        return mymap.values()
