# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return None
        nxt = self.insertionSortList(head.next)
        head.next= None
        return self.insert(head, nxt)

    def insert(self, curr, lst):
        if lst is None:
            return curr
        if curr.val <= lst.val:
            curr.next = lst
            return curr
        else:
            lst.next = self.insert(curr, lst.next)
            return lst

sol = Solution()
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(34)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(390)

node = sol.insertionSortList(head)
while node is not None:
    print node.val
    node = node.next
