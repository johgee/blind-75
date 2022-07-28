# input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# output: 6
# explanation: the lca of nodes 2 and 8 is 6



# definition for a binary tree node.
class TreeNode:
  def __init__(self, x, left, right):
      self.val = x 
      self.left = None
      self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      if (root == p or root == q or not root): 
        return root
      left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
      if left and right: 
        return root 
      elif left:
        return left 
      elif right:
        return right 
      return None 

root = [6,2,8,0,4,7,9,3,5]
p = 2
q = 8
ob1 = Solution()
print(ob1.lowestCommonAncestor(root, p, q))