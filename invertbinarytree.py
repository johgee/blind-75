class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self,right = right 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None 
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root 
  
root = [4, 2, 7, 1, 3, 6, 9]
ob1 = Solution()
print(ob1.invertTree(root))