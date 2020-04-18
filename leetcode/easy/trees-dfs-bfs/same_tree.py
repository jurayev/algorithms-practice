# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """BSF: time complexity O(n). Space O(n)"""
        if not root: return True
        return self.isMirrow(root.left, root.right)

    def isMirrow(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        # print(f"{root1.val} == {root2.val}")
        return (root1.val == root2.val
                and self.isMirrow(root1.left, root2.right)
                and self.isMirrow(root1.right, root2.left))


tree = [1, 2, 2, 3, 4, 4, 3]
