# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        prev = self.findNodeFromEnd(dummy, n + 1)
        prev.next = prev.next.next
        return dummy.next
    def findNodeFromEnd(self, head, n):
        tail = head
        while n != 0:
            tail= tail.next
            n = n - 1
        curr = head
        while tail != None:
            curr = curr.next
            tail = tail.next
        return curr

sol = Solution()
head = ListNode(1)
ans = sol.removeNthFromEnd(head, 1)
print("should be none")
while ans is not None:
    print(ans.val)
    ans = ans.next

print("end")

head = ListNode(1)
head.next = ListNode(2)
ans = sol.removeNthFromEnd(head, 1)
print("should be 2")
while ans is not None:
    print(ans.val)
    ans = ans.next

print("end")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
ans = sol.removeNthFromEnd(head, 3)
print("should be 2->3")
while ans is not None:
    print(ans.val)
    ans = ans.next

print("end")
