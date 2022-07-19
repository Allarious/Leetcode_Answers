
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class OddEvenList:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        even_head = head.next

        last_odd_node = self.odd_even_list_helper(head, None, None, True)
        last_odd_node.next = even_head

        return head


    def odd_even_list_helper(self, node, parent_node, grand_parent_node, is_odd):
        if grand_parent_node:
            grand_parent_node.next = node
        if not node.next:
            return node if is_odd else None
        next_node = node.next
        node.next = None
        last_odd_node = self.odd_even_list_helper(next_node, node, parent_node, not is_odd)
        if last_odd_node:
            return last_odd_node
        else:
            return node

    def convert_linked_list_to_array(self, head):
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return nums


if __name__ == "__main__":
    odd_even_list = OddEvenList()
    print(odd_even_list.convert_linked_list_to_array(odd_even_list.odd_even_list(ListNode(2, ListNode(9, ListNode(7))))))
