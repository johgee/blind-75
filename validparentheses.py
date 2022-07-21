class Solution:
  def isValid(self, s:str) -> bool:
      pair = {']':'[', '}':'{', ')':'('}
      curr = []
      for char in s: 
          if char in pair: 
              if len(curr) == 0 or curr.pop()!=pair[char]:
                  return False 
          else:
              curr.append(char)
      if len(curr)!=0:
          return False 
      return True 

input_list = "()"
# input_list = "()[]{}"
# input_list = "(]"
ob1 = Solution()
print(ob1.isValid(input_list))
