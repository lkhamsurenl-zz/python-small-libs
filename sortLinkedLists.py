# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        # find a middle node
        middle = self.findMiddle(head)
        if middle == None:
            return head
        # split into two parts
        fst = head
        snd = middle.next
        middle.next = None
        # recursively sort two
        sortedList1 = self.sortList(fst)
        sortedList2 = self.sortList(snd)
        # merge two ListNode
        return self.merge(sortedList1, sortedList2)

    def findMiddle(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nxt = dummy
        while nxt is not None and nxt.next is not  None:
            curr = curr.next
            nxt = nxt.next.next
        return curr

    def merge(self, lst1, lst2):
        if lst1 is None:
            return lst2
        if lst2 is None:
            return lst1
        if lst2.val < lst1.val:
            temp = lst1
            lst1 = lst2
            lst2 = temp
        # lst1 is always small
        head = lst1
        while not lst1.next == None and not lst2 == None:
            if lst1.next.val > lst2.val:
                temp = lst1.next
                lst1.next = lst2
                lst2 = temp
            lst1 = lst1.next
        if lst1.next == None:
            lst1.next = lst2
        return head


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(5)
node = head

sol = Solution()
currNode = sol.sortList(head)
while currNode is not None:
    print currNode.val
    currNode = currNode.next
