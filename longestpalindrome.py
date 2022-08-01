# given a string 's' which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# *letters are case sensitive, 'Aa' is not considered a palindrome here.

# input: s = "abccccdd"
# output: 7 
# explanation: one longest palindrome that can be built is "dccaccd", whose length is 7

# input: s = "a"
# output: 1
# explanation: the longest palindrome that can be built is "a", whose length is 1

# import collections # not working, need to check

# class Solution:
#     def longestPalindrome(self, s):
#         ans = 0
#         for v in collections.Counter(s).itervalues():
#             ans += v / 2 * 2
#             if ans % 2 == 0 and v % 2 == 1:
#                 ans += 1
#         return ans   

# s = "abcccdd"
# ob1 = Solution()
# print(ob1.longestPalindrome(s))

# from collections import Counter

# class Solution:
#     def longestPalindrome(self, s):
#         count = Counter(s) # counting all numbers in the format {'char': 'count'}
#         is_one = False # flag indicating whether there was 1 character that can be placed in the middleof the palindrome 
#         res = 0
#         for v in count.values():
#             if v % 2 == 1:
#                 is_one = True 
#             res += v - v % 2 # making an even number
        
#         return res + is_one # is_one - bool (False = 0, True = 1)

# s = "abcccdd"
# ob1 = Solution()
# print(ob1.longestPalindrome(s))

class Solution:
    def longestPalindrome(self, s):
        pairs = 0 
        unpaired_chars = set()

        for char in s:
            if char in unpaired_chars: 
                pairs += 1 
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return pairs * 2 + 1 if unpaired_chars else pairs * 2

s = "abcccdd"
ob1 = Solution()
print(ob1.longestPalindrome(s))