from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedListII:
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 0
        prev_node = None
        node = head
        left_side_node = None
        right_side_node = None
        left_link_node = None
        right_link_node = None

        if node is None:
            return None
        if node.next is None:
            return node
        if left == right:
            return node

        while node:
            i += 1
            if i == left:
                left_link_node = node
            elif i == right:
                right_link_node = node
            elif i == left - 1:
                left_side_node = node
            elif i == right + 1:
                right_side_node = node
            elif i > right + 1:
                break

            next_node = node.next
            if left <= i <= right:
                node.next = prev_node
            prev_node = node
            node = next_node

        if left_side_node:
            left_side_node.next = right_link_node
        left_link_node.next = right_side_node

        return head if left_side_node else right_link_node

if __name__ == "__main__":
    pass