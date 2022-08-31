"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Stage 1: interweave
        # Make a deep copy of each node and interweave them in the original list
        # Old List: A --> B --> C --> D
        # InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
        cur = head
        while cur:
            copy = Node(cur.val) #make a deep copy of the node
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next #skip interweaved nodes
      
                        
        # Stage 2: connect random pointers       
        # Now we can connect random pointers
        #
        # [*cur]    [*cur.next]               [*cur.random]   [*cur.random.next]
        #    A --------> A'------> B --> B' -------> C -------------> C'----------> D --> D'
        #    ^---------------------------------------^
        #           random pointer ^
        cur = head
        while cur:
            if cur.random: #check if the current node has a random pointer
                cur.next.random = cur.random.next
            cur = cur.next.next # skip interweave (A]) copy nodes
        
                        
        # Stage 3: remove old nodes               
        # Now we sepearate the interweaved pointers and make them into a new list
        cur = head
        dummy = Node(0)                                                                   
        prev = dummy 
        
        while cur:
            prev.next = cur.next
            cur.next = cur.next.next #point to next original pointer, as copy.next was the interweaved node
            cur = cur.next
            prev = prev.next #advance dummy list to current node at the dummy list :)
        
        return dummy.next
