# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        reversedTail = dummy
        currNode = head
        currTail = head
        distanceFromTail = k
        while currTail is not None:
            while distanceFromTail is not 0 and currTail is not None:
                currTail = currTail.next
                distanceFromTail = distanceFromTail - 1
            if currTail is None and distanceFromTail is not 0:
                reversedTail.next = currNode
                return dummy.next
            # Do reverse
            newTail  = currNode
            while currNode is not currTail:
                temp = currNode.next
                currNode.next = reversedTail.next
                reversedTail.next = currNode
                currNode = temp

            reversedTail = newTail # since we finished reversing current k elt
            distanceFromTail = k

        # we hit the end of the list
        # Do reverse
        #newTail  = currNode
        #while currNode is not currTail:
        #    temp = currNode.next
        #    currNode.next = reversedTail.next
        #    reversedTail.next = currNode
        #    currNode = temp
        return dummy.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
#head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)

reverse = sol.reverseKGroup(head, 2)
while reverse is not None:
    print reverse.val
    reverse = reverse.next
