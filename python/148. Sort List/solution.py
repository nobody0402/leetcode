# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next :
            return head
        
        mid = self.getMid(head)
        return self.merge(self.sortList(head),self.sortList(mid))
        
        
        
    def getMid(self, head):        
        pre = slow = fast = head
        
        while fast and fast.next:
            pre = slow
            slow = slow.next 
            fast = fast.next.next
        pre.next = None
        return slow
    
    def merge(self, left,right):
        result = p = ListNode(0)
        while left and right :
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        
        if left :
            p.next = left
        else :
            p.next = right
        
        return result.next