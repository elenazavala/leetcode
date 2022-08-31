# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #Three pointers
        prev = None
        curr = head
        
        #To reverse the list, the current's next has to point the previous node
        # prev    curr     next
        # 1   ->   2   ->   3
        
        #    2 -> 1
        
        while curr:
            nextp = curr.next #store next pointer so we dont lose it
            curr.next = prev #reverse
            prev = curr #advance list
            curr =  nextp #advance list
        #prev pointer is equal to the new head
        return prev
