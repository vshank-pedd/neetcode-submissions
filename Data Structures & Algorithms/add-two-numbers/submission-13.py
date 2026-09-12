# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        carry_over = False

        sol_node = ListNode()      # dummy head
        sol = sol_node

        while (l1_curr is not None or l2_curr is not None or carry_over):
            if (l1_curr is not None):
                first = l1_curr.val
            else:
                first = 0

            if (l2_curr is not None):
                second = l2_curr.val
            else:
                second = 0

            node_sum = first + second
            if (carry_over):
                node_sum = node_sum + 1

            if (node_sum >= 10):
                carry_over = True
                node_sum = node_sum - 10
            else:
                carry_over = False

            sol.next = ListNode(node_sum)
            sol = sol.next

            if (l1_curr is not None):
                l1_curr = l1_curr.next
            if (l2_curr is not None):
                l2_curr = l2_curr.next

        return sol_node.next