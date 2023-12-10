class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if root == p or root == q:
            return root
        elif left and right:
            return root
        return left or right