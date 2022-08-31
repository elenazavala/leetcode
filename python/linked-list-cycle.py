# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # we are shifting fast by TWO so we also need to check
        # fot fast.next
        while fast and fast.next: # While fast has not reached a nullptr
            slow = slow.next # increment slow by 1
            fast = fast.next.next #increment fast by 2
            
            #once they meet...
            if fast == slow:
                return True
            
        return False # This means fast has reached nullptr
