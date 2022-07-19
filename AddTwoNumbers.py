# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # node1 = self._reverse_linked_list(l1)
        # node2 = self._reverse_linked_list(l2)
        node1 = l1
        node2 = l2

        sum_result = ListNode()
        head = sum_result
        carry_one = False
        prev_node = None

        while node1 is not None or node2 is not None:

            value1 = node1.val if node1 else 0
            value2 = node2.val if node2 else 0
            # print(value1, value2)
            s = value1 + value2 + (1 if carry_one else 0)

            sum_result.val = s % 10
            carry_one = (s >= 10)

            sum_result.next = ListNode()
            prev_node = sum_result
            sum_result = sum_result.next

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

        if carry_one:
            sum_result.val = 1
        else:
            prev_node.next = None

        # return self._reverse_linked_list(head)
        return head

    def _reverse_linked_list(self, node: Optional[ListNode], previous_node=None):
        if node.next is None:
            node.next = previous_node
            return node

        head_node = self._reverse_linked_list(node.next, node)
        node.next = previous_node
        return head_node

    def convert_linked_list_to_array(self, head):
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return nums


if __name__ == "__main__":
    addTwoLinkedLists = AddTwoNumbers()
    print(addTwoLinkedLists.convert_linked_list_to_array(addTwoLinkedLists.add_two_numbers(ListNode(2, ListNode(9, ListNode(7))), ListNode(8, ListNode(6, ListNode(3))))))
