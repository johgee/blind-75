from curses.panel import top_panel


# -when climbing a staircase, it takes n steps to reach top_panel
# -each time you can either climb 1 or 2 steps 
# Q: how many distinct ways can you climb to the top?

# intput: n = 2
# output: 2 
# explanation: there are two ways to climb to the top 
# 1. 1 step + 1 step 
# 2. 2 steps 

# intput: n = 3
# output: 3 
# explanation: there are three ways to climb to the top 
# 1. 1 step + 1 step + 1 step 
# 2. 1 step + 2 steps 
# 3. 2 steps + 1 step 

# KINDA like fibonacci 

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n -1):
            temp = one 
            one = one + two 
            two = temp 

        return one  


n = 5
ob1 = Solution()
print(ob1.climbStairs(n))