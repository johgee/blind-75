# input: intervals = [[1,3], [6,9]], newInterval = [2,5]
# output: [[1,5], [6,9]]

# intput: intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]], newInterval = [4,8]
# output: [[1,2], [3,10], [12,16]]
# explanation: because the new interval [4,8] overlaps with [3,5], [6,7],[8,10]

# from typing import List

# class solution:
#     def insert(self, intervals: List[List[int]], neInterval: List[int]) -> List[List[[int]]]

class Solution:
    def insert(self, intervals, I):
        res, i = [], -1 
        for i, (x,y) in enumerate(intervals):
            if y < I[0]:
                res.append([x,y])
            elif I[1] < x:
                i -= 1
                break
            else: 
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
        
        return res + [I] + intervals[i+1:]

intervals = [[1,3], [6,9]]
newInterval = [2,5]
ob1 = Solution()
print(ob1.insert(intervals, newInterval))

# 1. interval [1,2] is before [4,8], that is y < I[0], so we just add it to our res 
# 2. interval [3,5] is not before [4,8] but not after also, so it is the third cse and we need to update I:I = [3,8]
# 3. interval [6,7] :the same logic, update I = [3,8] now (it did not change tho)
# 4. interval [8,10] :still condition number 3, so I = [3,10]
# 5. interval [12,16] it is after our I, so this is condition number 2 and we break from our loop: i = 3 
# 6. outside loop we combine res = [1,2], I = [3,10] and intervals[4:] = [12,16]

# time complexity: O(n)
# space complexity: O(n)

# by DBabichev 