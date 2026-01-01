from typing import Optional,List
class Node:
    def __init__(self, val:Optional[int]= None,children:Optional[List['Node']] = None):
        self.val = val
        self.children = children
        
        
class Solution:
    def __init__(self):
        self.preorderList = []
    def Traversal(self,root:Optional['Node']):
        if not root :
            return
        self.preorderList.append(root.val)

        for i in root.children or []:
            self.Traversal(i)
        
    def preorder(self,root:'Node') -> List[int]:
        self.Traversal(root)
        return self.preorderList


node4 = Node(4)
node2 = Node(2)    
node5 = Node(5)
node6= Node(6)
node3 = Node(3 , [node5,node6])
node1 = Node(1 ,[node3,node2,node4])
solve = Solution()
print(solve.preorder(node1))