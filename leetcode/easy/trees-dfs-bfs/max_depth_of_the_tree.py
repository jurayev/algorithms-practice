class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def max_depth(self, node: TreeNode) -> int:
        if not node: return 0
        if not node.left and not node.right: return 1
        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        return max(left, right) + 1

sol = Solution()


