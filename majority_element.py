# given an array nums of size n, return the majority element

# the majority element is the element that appears more than [n/2] times.
# you may assume that the majority element always exists in the array.

# input: nums = [3, 2, 3]
# output: 3

# input: nums = [2, 2, 1, 1, 1, 2, 2]
# output: 2

# Approach 1: Brute Force 

# time complexity: O(n^2)
# space complexity: O(1)

# class Solution:
#     def majorityElement(self, nums):
#         majority_count = len(nums)//2
#         for num in nums:
#             count = sum(1 for elem in nums if elem == num)
#             if count > majority_count:
#                 return num 

# nums = [3, 2, 3]
# ob1 = Solution()
# print(ob1.majorityElement(nums))

# 2: HashMap

# time complexity: O(n)
# space complexity: O(n)

# import collections 

# class Solution:
#     def majorityElement(self, nums):
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key = counts.get)

# nums = [3, 2, 3]
# ob1 = Solution()
# print(ob1.majorityElement(nums))

# 3: sorting

# time complexity: O(nlgn)
# space complexity: O(1) or (O(n))

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

nums = [3, 2, 3]
ob1 = Solution()
print(ob1.majorityElement(nums))