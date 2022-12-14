# 19/19. REMOVE NTH NODE FROM END OF LIST

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# - pseudo -
# fast, slow = head, head
# for _ in range(n): fast = fast.next
# if not fast: return head.next
# while fast.next: fast, slow = fast.next, slow.next
# slow.next = slow.next.next
# return 

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
          fast = fast.next
        if not fast: 
          return head.next
        while fast.next:
          fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head