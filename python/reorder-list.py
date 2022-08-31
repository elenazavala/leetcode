# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # very hard problem
        
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now slow points at 2, so slow.next will be the beginning of our second list
        second = slow.next # save beginning of second list
        slow.next = None # now we can split the first list as [1,2]
        
        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # after the loop, the previous pointer is the new head of the second half of the list, somehow, dont ask me how
         
        # merge two halfs by alternating first and second values
        first, second = head, prev
        
        #in each step we modify two nodes
        while second:
            #store
            temp1, temp2 = first.next, second.next
            #merge
            first.next = second
            second.next = temp1
            #shift pointers
            first, second = temp1, temp2
