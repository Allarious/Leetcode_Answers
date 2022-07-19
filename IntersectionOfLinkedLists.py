
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class IntersectionLinkedLists:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        if not self.have_intersection(headA, headB):
            return None

        len_linked_B = self.len_linked_list(headB)
        len_linked_A = self.len_linked_list(headA)

        end_head = self.reverse_linked_list(headA)
        print(end_head.val)

        new_len_linked_B = self.len_linked_list(headB)
        print(new_len_linked_B, len_linked_B)

        intersection_length = int((len_linked_B + len_linked_A - new_len_linked_B) / 2)

        # if intersection_length == 0:
        #     return None

        node = end_head
        for i in range(intersection_length):
            node = node.next

        self.reverse_linked_list(end_head)

        return node

    def reverse_linked_list(self, node, prev_node=None):
        if node.next is None:
            node.next = prev_node
            return node
        end_head = self.reverse_linked_list(node.next, node)
        node.next = prev_node
        return end_head

    def len_linked_list(self, node):
        if node is None:
            return 0
        length = 1
        while node.next:
            length += 1
            node = node.next
        return length

    def have_intersection(self, nodeA, nodeB):
        while nodeA.next or nodeB.next:
            nodeA = nodeA.next if nodeA.next else nodeA
            nodeB = nodeB.next if nodeB.next else nodeB
        return nodeA.val == nodeB.val




if __name__ == "__main__":
    pass