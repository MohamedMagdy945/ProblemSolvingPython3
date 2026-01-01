from typing import Optional,List
class Node:
    def __init__(self, val:Optional[int]= None,children:Optional[List['Node']] = None):
        self.val = val
        self.children = children
        
        
class Solution:
    def __init__(self):
        self.postorderList = []
    def Traversal(self,root:Optional['Node']):
        if not root :
            return

        for i in root.children or []:
            self.Traversal(i)
        self.postorderList.append(root.val)

    def postorder(self,root:'Node') -> List[int]:
        self.Traversal(root)
        return self.postorderList


node4 = Node(4)
node2 = Node(2)    
node5 = Node(5)
node6= Node(6)
node3 = Node(3 , [node5,node6])
node1 = Node(1 ,[node3,node2,node4])
solve = Solution()
print(solve.postorder(node1))