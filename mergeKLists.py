from heapq import heappush, heappop
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        gHead = ListNode(-1)
        curr = gHead
        h = []
        # initialize
        for i in range(len(lists)):
            head = lists[i]
            heappush(h, (head.val, head, i))
            lists[i] = lists[i].next
        while len(h) != 0:
            (val, node, index) = heappop(h)
            curr.next = node
            curr = curr.next
            if lists[index] != None:
                nd = lists[index]
                heappush(h, (nd.val, nd, index))
                lists[index] = lists[index].next
        return gHead.next


sol = Solution()
head1 = ListNode(1)
head1.next = ListNode(5)
head1.next.next = ListNode(6)

head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(20)

head3 = ListNode(4)
head3.next = ListNode(7)
head3.next.next = ListNode(9)
head3.next.next.next = ListNode(11)

so = sol.mergeKLists([head1, head2, head3])
while so != None:
    print so.val
    so = so.next
