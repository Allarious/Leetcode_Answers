
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class PartitionList:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        node = head
        lhead = None
        gehead = None
        lnode = None
        genode = None

        while node:
            if node.val < x:
                if lhead is None:
                    lhead = node
                # if less than x
                if lnode:
                    lnode.next = node
                    lnode = node
                else:
                    lnode = node
            else:
                if gehead is None:
                    gehead = node
                # if greater than or equal to x
                if genode:
                    genode.next = node
                    genode = node
                else:
                    genode = node

            next_node = node.next
            node.next = None
            node = next_node

        if lnode:
            lnode.next = gehead

        return lhead if lhead else gehead

if __name__ == "__main__":
    pass