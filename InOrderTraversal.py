
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InorderTraversal:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left_tree_traversal = self.inorder_traversal(root.left)
        right_tree_traversal = self.inorder_traversal(root.right)
        return left_tree_traversal + [root.val] + right_tree_traversal

if __name__ == "__main__":
    pass