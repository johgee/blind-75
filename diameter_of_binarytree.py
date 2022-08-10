# given the root of a binary tree, return the length of the diameter of the tree 

# the diameter of a binary tree is the length of the longest path between any two nodes in a tree. this path may or may not pass through the root.

# the length of a path between two nodes is represented by the number of edges between them.

# input: root = [1,2,3,4,5]
# output: 3
# explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3]

# input: root [1,2]
# output: 1 

# definition for a binary tree node.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]

    def depth(self, root, diameter):
        if not root:
            return 0
        left_height = self.depth(root.left, diameter)
        right_height = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)

root = [1,2]
ob1 = Solution()
print(ob1.diameterOfBinaryTree(root))