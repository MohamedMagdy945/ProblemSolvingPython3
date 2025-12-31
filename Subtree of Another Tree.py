from typing import Optional
class TreeNode:
    def __init__(self ,val =0 ,left= None ,right =None):
        self.val = val
        self.left =left
        self.right = right
        
class Solution:
    def isSametree(self , node1:Optional[TreeNode], node2:Optional[TreeNode]) -> bool:
        if not node1 and not node2 :
            return True
        if not node1 or not node2 :
            return False
        return node1.val == node2.val and self.isSametree(node1.left,node2.left) and self.isSametree(node1.right,node2.right)
    
    def isSubtree(self, root:Optional[TreeNode],subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if (self.isSametree(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
node5 = TreeNode(5)
node2 = TreeNode(2)
node1 = TreeNode(1)
node4 = TreeNode(4,node1, node2)
root = TreeNode(3,node4,node5)

subNode2 = TreeNode(2)
subNode1 = TreeNode(1)
subNode4 = TreeNode(4,subNode1,subNode2)

solve = Solution()
print(solve.isSubtree(root,subNode4))