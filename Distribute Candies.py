from typing import List
class Solution:
    def distributeCandies(self,candyType:List[int])-> int:
        uniqueTypes = set(candyType)

    
        return min(len(uniqueTypes) , len(candyType) // 2)