# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        root = ListNode(-1) # dummy value representing the root
        curr = root
        offset = 0
        while l1 != None and l2 != None:
            curr.next = ListNode((l1.val + l2.val + offset) % 10)
            offset = (l1.val + l2.val + offset) / 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1 != None:
            curr.next = ListNode((l1.val + offset) % 10)
            offset = (l1.val + offset) / 10
            l1 = l1.next
            curr= curr.next
        while l2 != None:
            curr.next = ListNode((l2.val + offset) % 10)
            offset = (l2.val + offset) / 10
            l2 = l2.next
            curr = curr.next
        if offset != 0:
            curr.next = ListNode(offset)
        return root.next

sol = Solution()
l1 = ListNode(9)
l1.next = ListNode(2)
l1.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(5)

l = sol.addTwoNumbers(l1, l2)
while l != None:
    print l.val
    l = l.next
