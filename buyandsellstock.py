from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0
    buy = prices[0]
    for price in prices[1:]:
      if price < buy:
        buy = price 
      elif price - buy > maxProfit: 
        maxProfit = price - buy
    return maxProfit 

input_list = [7, 1, 5, 3, 6, 4]
ob1 = Solution()
print(ob1.maxProfit(input_list))
