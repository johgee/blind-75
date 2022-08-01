# input: head = [1, 2, 3, 4, 5]
# output: [5, 4, 3, 2, 1]

# input: head = [1, 2]
# output: [2. 1]

# input: head = []
# output: []

# definition for singly-linked list.

from typing import Optional 

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        curr = head 
        prev = None 
        while curr:
            next = curr.next 
            curr.next = prev 
            # update stages 
            prev = curr
            curr = next 
        return prev 
  
head = [1, 2, 3, 4, 5]
ob1 = Solution()
print(ob1.reverseList(head))
# it says 'list' object has no attribute 'next'