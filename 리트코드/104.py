from collections import deque

# Level Order Traversal (레벨 순회)
class Solution(object):
    def maxDepth(self, root):
        max_depth = 0
        if root is None:
            return max_depth
        
        q = deque()
        q.append((root, 1))

        while q:
            curr, curr_depth = q.popleft()
            max_depth = max(max_depth, curr_depth)

            if curr.left:
                q.append((curr.left, curr_depth + 1))
            if curr.right:
                q.append((curr.right, curr_depth + 1))

        return max_depth
    
# Postorder (후위순회)
class Solution(object):
    def maxDepth(self, root):
        max_depth = 0

        if root is None:
            return max_depth

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1