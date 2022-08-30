# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = []
        self.kthSmallestHelper(root, k, array)
        
        return array[k-1]
        
    def kthSmallestHelper(self, root, k, array):
        if root is None:
            return 
        self.kthSmallestHelper(root.left, k, array)
        array.append(root.val)   
        self.kthSmallestHelper(root.right, k, array)        
        
        
        
#         stack = []
#         count = 0
#         curr = root
        
#         while stack or curr:
            
#             if curr:
#                 stack.append(curr)
#                 curr = curr.left
#             else:
#                 curr = stack.pop()
#                 possibleValue = curr.val
#                 curr = curr.right
#                 count += 1
            
#             if count == k:
#                 return possibleValue
            
#         return None
