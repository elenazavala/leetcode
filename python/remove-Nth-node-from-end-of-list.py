# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # dummy nodes are variables we use as placeholders to the beginning  of a list
        # they point to the head, so that we can easily return them later
        
        dummy = ListNode()
        dummy.next = head
        
        # [*prev]   [*head]
        # dummy   ->   1   ->    2  ->   3
        curr = head
        prev = dummy
        
        # get list length
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        
        position = count - n # Since indeces start from 0, if we do #ofNodes - n we get the actual position starting from the beginnin
        
        # Let's do a while loop where we will end up at the node WE WANT to delete
        while(position > 0):
            prev = curr
            curr = curr.next
            position -= 1
        
        prev.next = curr.next
        return dummy.next
        
       
        # Mi forma tontita de hacer antes lo mismo que arriba..funciona igual
        # delete node at *position*
        # finder = 0
        # while(curr):
        #     print(curr.val)
        #     if finder == position: #if we arrived at the position
        #         prev.next = curr.next #grab the previous node from the one we want to delete, and make the next one of previous be the next one of current we want to delete
        #     else:
        #         curr = curr.next
        #     finder+=1
