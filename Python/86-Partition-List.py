# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x):
        lessHead = less = ListNode(-1)
        greatHead = great = ListNode(-1)
        while head:
            if head.val < x:
                less.next = less = head
            else:
                great.next = great = head
            head = head.next
        less.next, great.next = greatHead.next, None
        return lessHead.next
        