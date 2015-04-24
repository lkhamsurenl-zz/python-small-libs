# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(-1) # dummy value
        dummy.next = head
        curr = dummy
        while curr.next != None:
            if curr.next.val == val:
                curr.next  = curr.next.next # remove curr.next
            else:
                curr = curr.next
        return dummy.next

sol = Solution()
head = ListNode(1)
head.next= ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)
curr = sol.removeElements(head, 1)
while curr != None:
    print curr.val
    curr = curr.next
