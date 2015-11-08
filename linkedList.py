# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next == None:
            return str(self.val)
        return "{}->{}".format(self.val, self.next)

class LL(object):
    def fromList(self, lst):
        head = ListNode(-1) # dummy head
        curr = head # iterator
        i = 0 # iterator on lst
        while i < len(lst):
            curr.next = ListNode(lst[i])
            i += 1
            curr = curr.next
        return head.next

    def equal(self, head1, head2):
        if head1 == None or head2 == None:
            return head1 == head2 # since at least one is None, they should be same
        return head1.val == head2.val and self.equal(head1.next, head2.next)

    # check if LL is a palindrome
    def isPalindrome(self, head):
        # find the middle element
        mid = self.findMiddle(head)
        sHead = mid.next
        mid.next = None
        # reverse the second half
        rHead = self.reverse(sHead)
        # check if they are equal
        while rHead != None and head != None:
            if rHead.val != head.val:
                return False
            rHead = rHead.next
            head = head.next
        return True

    # find middle of linked list
    def findMiddle(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    # reverse a given LL
    def reverse(self, head):
        dummy = ListNode(-1) # dummy value
        while head != None:
            temp = dummy.next # save the chain
            dummy.next = head
            head = head.next
            dummy.next.next = temp
        return dummy.next

    # find Nth lsat element of LL
    def findNthLast(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while n != 0 and curr != None:
            curr = curr.next
            n = n - 1
        nth = dummy
        last = curr
        while last != None:
            nth = nth.next
            last = last.next
        return nth

    def removeNthLast(self, head, n):
        """
        removeNthLast element in the given LL, 1 <= n <= len
        """
        # Find the n + 1 the last element, then remove next one
        dummy = ListNode(-1) # dummy head
        dummy.next = head
        prev = self.findNthLast(dummy, n + 1)
        # fix the next pointer
        prev.next = prev.next.next
        return dummy.next

    def mergeSorted(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        # ensure head1 value is always smaller than that of head2
        if head1.val > head2.val:
            temp = head1
            head1 = head2
            head2 = temp
        head = head1 # this will be the head after merging
        while head1.next != None and head2 != None:
            # compare values in head1.next and head2
            if head2.val < head1.next.val:
                temp = head1.next
                head1.next = head2
                head2 = temp
            head1 = head1.next
        # If head2 is not done, just join since head1.next is None.
        if head2 != None:
            head1.next = head2
        return head

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        mid = self.findMiddle(head)
        head2 = mid.next
        mid.next = None
        return self.mergeSorted(self.mergeSort(head), self.mergeSort(head2))

    def linkedListCopy(self, head):
        """
        Given a linked list with pointers, copy
        """
        curr = head
        dummy = ListNode(None)
        copyMap = {}
        copyCurr = dummy
        while curr != None:
            if curr not in copyMap:
                copyCurr.next = ListNode(None)
                copyMap[curr] = copyCurr.next # add to the map 
            if curr.val not in copyMap:
                copyCurr.next.val = ListNode(None)
                copyMap[curr.val] = copyCurr.next.val
            else:
                copyCurr.next.val = copyMap[curr.val]
            curr = curr.next
            copyCurr = copyCurr.next
        return dummy.next

################################ TEST   #############################
ll = LL()
############################### reverse test ##########################
for (l, w) in [ ([1,2,3], [3,2,1]), ([1], [1]) ]:
    head = ll.fromList(l)
    want = ll.fromList(w)
    got = ll.reverse(head)
    assert ll.equal(got, want), \
        "reverse({}) = {}; want {}".format(head, got, want)

############################### find Middle ##########################
for (l, w) in [ ([1,2,3], 2), ([1,2,3,1], 2) ]:
    head = ll.fromList(l)
    got = ll.findMiddle(head)
    want = ListNode(w)
    assert (got == None and want == None) or got.val == want.val, \
        "findMiddle({}) = {}; want {}".format(head, got.val, want)

############################### Nth last test ##########################
for (l, i, w) in [ ([1,2,3], 1, 3), ([1,2,3], 2, 2), ([1,2,3], 3, 1), ([1], 1, 1) ]:
    head = ll.fromList(l)
    got = ll.findNthLast(head, i)
    want = ListNode(w)
    assert (got == None and want == None) or got.val == want.val, \
        "findNthLast({}, {}) = {}; want {}".format(head, i, got, want)

############################### remove Nth last test ##########################
for (l, i, w) in [ ([1,2,3], 1, [1,2]), ([1,2,3], 2, [1,3]), ([1,2,3], 3, [2,3]), ([1], 1, []) ]:
    head = ll.fromList(l)
    got = ll.removeNthLast(head, i)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "removeNthLast({}, {}) = {}; want {}".format(head, i, got, want)

############################### is Palindrome ##########################
for (l, want) in [ ([1,2,3], False), ([1,2,2,1], True), ([1,2,3,2,1], True) ]:
    head = ll.fromList(l)
    got = ll.isPalindrome(head)
    assert got == want, \
        "isPalindrome({}) = {}; want {}".format(head, got, want)

############################### Merge sorted LL ##########################
for (l1, l2, w) in [ ([1], [2], [1,2]), ([], [], []), ([1,4,5], [2,3,6], [1,2,3,4,5,6]), ([2,3,6], [1,4,5], [1,2,3,4,5,6]) ]:
    head1 = ll.fromList(l1)
    head2 = ll.fromList(l2)
    got = ll.mergeSorted(head1, head2)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "mergeSorted({}, {}) = {}; want {}".format(head1, head2, got, want)

############################### Merge sort on LL ##########################
for (l, w) in [ ([], []), ([1,4,5, 2,3,6], [1,2,3,4,5,6]), ([2,3,6,1,4,5], [1,2,3,4,5,6]) ]:
    head = ll.fromList(l)
    got = ll.mergeSort(head)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "mergeSort({}) = {}; want {}".format(head, got, want)

########################### Linked list copy pointer ######################
print("linked list with pointer copy")
head = ListNode(None)
head.val = ListNode(None)
head.next = ListNode(None)
head.next.val = head
head.next.next = None

copy = ll.linkedListCopy(head)
assert(copy == copy.next.val)
assert(copy.next.next == None)

head = None
copy = ll.linkedListCopy(head)
assert(copy == None)
