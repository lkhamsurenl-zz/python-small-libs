# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        [node1, node2] = self.findKthLast(head, k)
        if node1.next is head:
            return head
        node2.next = head
        ret = node1.next
        node1.next = None
        return ret

    def findKthLast(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast is not None and k != 0:
            fast = fast.next
            k = k - 1
        if fast is None:
            return None # since there is not enough elements in the list
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return [slow, fast]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()

rotated = sol.rotateRight(head,3)
while rotated is not None:
    print rotated.val
    rotated = rotated.next
