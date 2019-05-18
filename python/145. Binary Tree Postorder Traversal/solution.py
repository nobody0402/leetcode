# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        
        cur = root
        stack = []
        res = []
        while cur or stack:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            if stack and cur.right is stack[-1]:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                res.append(cur.val)
                cur = None
                
        return res