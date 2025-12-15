#https://leetcode.com/problems/kth-smallest-element-in-a-bst/?difficulty=MEDIUM

class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_vals = inorder(root)
        return sorted_vals[k - 1]
