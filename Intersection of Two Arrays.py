from typing import List
class Solution:
    def intersection(self,nums1:List[int],nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        
        solve = set()
        for i in st1:
            if (i in st2):
                solve.add(i)
                
        return list(solve)
    
    
solve = Solution()

print(solve.intersection([1, 2, 2,1],[2,2]))