# Problem link -> https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    @staticmethod
    def dfs(node, path):
        if not node:                                # If the node null
            return 0
        
        path = (path<<1) + node.val                 # append value of the node to the path
        
        if (not node.left) and (not node.right):    # if the node is leaf node
            return path                             # simply return calculated path
        
        return Solution.dfs(node.left, path) + Solution.dfs(node.right, path)    
        # node will have atleast one child so return 
        # "the path from the current node to left leaf child" and 
        # "the path from the current node to right leaf child"
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return Solution.dfs(root, 0)    # initially the path is 0 or we can assume empty
    
    