#merge two arrays

class ListNode:
  def __init__(self, val=0, next = None):
      self.val = val 
      self.next = next 
class Solution:
  def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
      dummy = cursor = ListNode(0)
      while list1 and list2: 
          if list1.val < list2.val:
            cursor.next = list1 
            list1 = list1.next
          else:
            cursor,next = list2 
            list2 = list2.next 
          cursor = cursor.next 
      if (list1 == None) or (list2 == None):
          cursor.next = list1 or list2
      return dummy.next 


list1 = [1, 2, 4]
list2 = [1, 3, 4]
ob1 = Solution()
print(ob1.mergeTwoLists(list1, list2))