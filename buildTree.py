
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BuildTree:
    def __init__(self):
        self.hashmap = {}
        self.preorder = []
        self.inorder = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.preorder = preorder
        for index, val in enumerate(inorder):
            self.hashmap[val] = index
        return self.build_tree_helper(0, 0, len(inorder) - 1)

    def build_tree_helper(self, preorder_root, inorder_left, inorder_right) -> Optional[TreeNode]:

        if preorder_root >= len(self.preorder) or inorder_left > inorder_right:
            return None

        if inorder_left == inorder_right:
            return TreeNode(self.inorder[inorder_left])

        inorder_root = self.hashmap[self.preorder[preorder_root]]
        number_in_left_tree = inorder_root - inorder_left
        number_in_right_tree = inorder_right - inorder_root

        return TreeNode(self.preorder[preorder_root],
                        self.build_tree_helper(
                            preorder_root + 1,
                            inorder_left,
                            inorder_root - 1
                        ),
                        self.build_tree_helper(
                            preorder_root + number_in_left_tree + 1,
                            inorder_left + number_in_left_tree + 1,
                            inorder_right
                        )
                        )


if __name__ == "__main__":
    print(BuildTree().build_tree([3,9,20,15,7], [9,3,15,20,7]))