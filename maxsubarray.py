# input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# output: 6
# explanation: [4, -1, 2, 1] has the largets sum = 6

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = 0
        total = 0
        for val in nums:
            total += val 
            if total >= max_val:
                max_val = total 
            elif total < 0:
                total = 0 
        if max_val == 0:
            return max(nums)
        return max_val 

num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ob1 = Solution()
print(ob1.maxSubArray(num))