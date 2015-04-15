# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        currList = head
        dummy = ListNode(0)
        currSwap = dummy
        while currList is not None and currList.next is not None:
            print currSwap.val
            temp = currList.next.next

            currSwap.next = currList.next
            currList.next.next = currList
            currList.next = None

            currList = temp
            currSwap = currSwap.next.next
        if currList is None:
            return dummy.next
        else:
            currSwap.next = currList
        return dummy.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
curr = sol.swapPairs(head)
while curr is not None:
    print curr.val
    curr  = curr.next
