# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head.next # slow moved by one
        fast = head.next.next # fast move by two
        while fast is not None and fast.next is not None:
            if slow.val == fast.val: # there is a cycle and slow is exactly as same length away from head to the start of the cycle
                curr = head
                print slow.val
                print fast.val
                while curr.val is not slow.val:
                    curr = curr.next
                    slow = slow.next
                return curr
            else:
                slow = slow.next
                fast = fast.next.next
        return None # there is no cycle

head = ListNode(-1)
head.next = ListNode(-7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(-4)
head.next.next.next.next = ListNode(19)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(-9)
head.next.next.next.next.next.next.next = ListNode(-5)
head.next.next.next.next.next.next.next.next = ListNode(-2)
head.next.next.next.next.next.next.next.next.next = head.next.next.next.next.next.next.next
curr = head

sol = Solution()
print sol.detectCycle(head).val
