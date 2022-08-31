# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution:
        # Two pointers: first and second initialized at head and the next of head
        # We loop length/2 times and swap elements
        
        curr,count = head, 0
        
        while curr:
            curr = curr.next
            count += 1
                
        if not head or count == 1: return head
            
        count = count // 2
        curr = head
        first, second = head, head.next

        while count > 0:
            temp = first.val
            first.val = second.val
            second.val = temp
            if second.next != None:
                first = second.next
                second = first.next
            count -= 1
     

        return head
        
