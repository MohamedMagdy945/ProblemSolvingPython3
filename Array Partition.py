from typing import List
class Solution:
    def arrayPairSum(self,nums:List[int])-> int:
        nums.sort()
        max_pair =0
        for i in range(0,len(nums),2):
            max_pair += nums[i]
        return max_pair
    
solve = Solution()
print(solve.arrayPairSum([6,2,6,5,1,2]))