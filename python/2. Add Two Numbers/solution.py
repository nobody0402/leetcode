# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = cur = ListNode(0)
        
        while l1 or l2 or carry:
            add = carry
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            
            carry = add // 10
            add = add % 10
            cur.next = ListNode(add)
            cur = cur.next
        
        return head.next