# 206/12. REVERSE LINKED LIST

# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Example : 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# in:  (1)->(2)->(3)->(4)->(5)
# out: (5)->(4)->(3)->(2)->(1)

# - pseudo -
# prev, cur = None, head
# while cur:
  # temp = cur.next
  # cur.next = prev
  # prev = cur
  # cur = temp
# return prev

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = None, head
        
        while cur:
          temp = cur.next
          cur.next = prev
          prev = cur
          cur = temp
        return prev
        
