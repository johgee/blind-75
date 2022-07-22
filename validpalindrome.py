# input: s = "A man, a plan, a canal: Panama"
# output: true 
# exaplanation: "amanplancanalpanama" is a palindrome 

class Solution:
  def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
      while not s[l].isalnum() and l < r:
        l += 1
      while not s[r].isalnum() and l < r:
        r -= 1
      if s[l].lower() != s[r].lower():
          return False 
      l += 1
      r -= 1
    return True 

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s= " "
ob1 = Solution()
print(ob1.isPalindrome(s))