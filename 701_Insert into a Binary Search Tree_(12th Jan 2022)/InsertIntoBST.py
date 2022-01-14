# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:                    # If the given BST is empty
            return TreeNode(val)        # Simply create and return new node with givan val
        
        pos = root                      # Copy the root 
        
        while True:
            
            if pos.val < val:           # If current val is less than val (Or we can say that val is greater than current val)
                                        # traverse to the right side of the given tree
                if pos.right:           # If right side is not empty go ahead
                    pos = pos.right
                    
                else:                   # If the right side is empty, then insert a new node and break
                    pos.right = TreeNode(val)
                    break
                
            else:                       # If current value id greater than val
                                        # Traverse to the left side
                if pos.left:            # If the left side is not an empty node, go on
                    pos = pos.left
                    
                else:                   # If the left side is empty, create a new node and break                    
                    pos.left = TreeNode(val)
                    break
                
        return root                     # Return the root of the tree