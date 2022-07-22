
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ZigzagInorder:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = [[root]]
        left_to_right = False
        while True:
            # print(result[-1][0].val)
            next_level = []
            last_level = result[-1][::-1]
            for node in last_level:
                print(node.val)
                if left_to_right:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            if len(next_level) == 0:
                break
            left_to_right = not left_to_right
            result.append(next_level)

        # print(result[-1][0].val)
        val_result = []
        for array in result:
            entry = []
            for node in array:
                entry.append(node.val)
            val_result.append(entry)

        return val_result



if __name__ == "__main__":
    pass


