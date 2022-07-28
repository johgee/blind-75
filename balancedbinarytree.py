# height balanced = a binary tree in which the left and right subtrees of ever ynode differ in height by no more than 1.

# input: root = [3,9,20,None,None,15,7]
# output: true 

# input: root [1,2,2,3,3,None,None,4,4]
# output: false

# input: root = []
# output: true 

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def get_heights(node):
#             if not node:
#                 return 0
#             if not node.right and not node.left:
#                 return 1
#             right = get_heights(node.right)
#             left = get_heights(node.left)
#             if abs(left - right) >= 2:
#                 raise Exception()
#             return max(left, right) + 1
#         try:
#             get_heights(root)
#             return True 
#         except Exception:
#             return False 


# solution 2

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True 

        l_height = self.height(root.left)
        r_height = self.height(root.right)

        if abs(l_height - r_height) > 1:
            return False 
        
        l_balance = self.isBalanced(root.left)
        r_balance = self.isBalanced(root.right)

        return l_balance and r_balance 
    
    def height(self, root):
        if root is None:
            return 0 
        else: 
            return 1 + max(self.height(root.left), self.height(root.right))
        
s = [3,9,20,None,None,15,7]
ob1 = Solution()
print(ob1.isBalanced(s))