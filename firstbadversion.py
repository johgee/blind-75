# input: n = 5, bad = 4
# output: 4
# explanation:
# call isBadVersion(3) -> false 
# call isBadVersion(5) -> true 
# call isBadVersion(4) -> true 
# Then 4 is the first bad version.

# input: n = 1, bad = 1
# output: 1

class Solution:
    def firstBadVersion(self, n: int) -> int: 
    # def firstBadVersion(self, n):
        left, right = 1, n 
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else: 
                left = mid + 1
        return left 

n = 1
bad = 1
ob1 = Solution()
print(ob1.firstBadVersion(n, bad))