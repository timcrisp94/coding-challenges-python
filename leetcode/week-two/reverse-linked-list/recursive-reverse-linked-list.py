# 206/12. REVERSE LINKED LIST
# * recursive (optimal) *

# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Example : 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# in:  (1)->(2)->(3)->(4)->(5)
# out: (5)->(4)->(3)->(2)->(1)

# - pseudo -
# def reverseList(self,head)
  # return self.helper(head, None)
# def helper(self, head, node)
  # if not head return node
  # temp = head.next
  # head.next = node
  # return self.helper(temp, head)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        return self.helper(head, None)
    
    def helper(self, head, node):
      if not head:
        return node
      temp = head.next
      head.next = node
      return self.helper(temp, head)