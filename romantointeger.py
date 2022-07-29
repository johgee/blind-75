# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# input: s = "III"
# output: 3
# explanation: III = 3

# input: s = "LVIII"
# output: 58
# explanation: L = 50, V = 5, III = 3

# input: s = "MCMXCIV"
# output: 1994
# explanation: M = 1000, CM = 900, CX = 90 and IV = 4

class Solution:
    def romanToInt(self, s: str) -> int:
        rd = {
          "I" : 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }

        n = len(s)
        rt = 0
        for i in range(n):
            if i == n - 1 or rd[s[i]] >= rd[s[i + 1]]:
                rt += rd[s[i]]
            else:
                rt -= rd[s[i]]
        return rt


s = "III"
ob1 = Solution()
print(ob1.romanToInt(s))