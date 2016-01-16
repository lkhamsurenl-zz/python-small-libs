from heapq import heappush, heappop
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

    def mergeKLists(self, heads):
        h = []
        for i in range(len(heads)):
            head = heads[i]
            if heads[i] != None:
                temp = head.next
                head.next = None
                heappush(h, (head.val, i, head))
                heads[i] = temp
        merged = ListNode(-1)
        curr = merged
        # as long as there is a elt in heap, remove and add from the same list
        while len(h) != 0:
            (v, i, top) = heappop(h) # pop the min value
            curr.next = top
            curr = curr.next
            if heads[i] != None: # add from the LL
                head = heads[i]
                temp = head.next
                head.next = None
                heappush(h, (head.val, i, head))
                heads[i] = temp
        return merged.next


    def swapInPairs(self, head):
        dummy = ListNode(-1) # dummy head
        curr = dummy
        while head != None and head.next != None:
            temp = head.next.next
            curr.next = head.next
            head.next.next = head
            head.next = None
            curr = head
            head = temp
        if head != None:
            curr.next = head
        return dummy.next 

    def rotateRight(self, head, k):
        """
        rotate a given LL right by k 
        """
        if k == 0 or head == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = self.findNthLast(dummy, k + 1)
        newHead = prev.next
        prev.next = None # break the chain
        runner = newHead
        while runner.next != None:
            runner = runner.next
        # runner is at the end
        runner.next = dummy.next
        return newHead

    def remove(self, head, value):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next != None:
            if curr.next.val == value:
                curr.next = curr.next.next # remove the next element
            else:
                curr = curr.next
        return dummy.next

    def mix(self, head):
        # if the head is length 0 or 1, then no mixing can be done.
        if head == None or head.next == None:
            return head
        # Find the middle, then reverse the second half.
        mid = self.findMiddle(head)
        head2 = mid.next
        mid.next = None
        # reverse the head2
        head2 = self.reverse(head2)
        dummy = ListNode(-1) # dummy head
        curr = dummy
        while head2 != None:
            # Join the first head.
            curr.next = head
            head = head.next
            curr = curr.next
            # Join the head of the second head.
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        # head is length equal to head2, or longer by one.
        if head != None:
            curr.next = head
        return dummy.next


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

    def addTwoLists(self, lst1, lst2):
        """
        Add a 2 given LL
        """
        if lst1 == None:
            return lst2
        if lst2 == None:
            return lst1
        offset = 0 # offset added to the next value
        dummy = ListNode(-1)
        curr = dummy # runner 
        while lst1 != None or lst2 != None or offset != 0:
            val = offset
            if lst1 != None:
                val += lst1.val
                lst1 = lst1.next
            if lst2 != None:
                val += lst2.val
                lst2 = lst2.next
            offset = val / 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def insertionSort(self, head):
        """
        Perform a insertionSort in a given arbitrary list
        """
        if head == None or head.next == None:
            return head
        node = head
        head = head.next
        node.next = None
        head = self.insertionSort(head)
        return self.insertToSorted(node, head)

    def insertToSorted(self, node, head):
        """
        Insert a given node to the sorted head.
        """
        if head == None:
            return node
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next != None and node.val > curr.next.val:
            curr = curr.next
        if curr.next == None:
            curr.next = node
            return head
        # Since node.val < curr.next.val, order shoudl be curr -> node -> curr.next
        temp = curr.next
        curr.next = node
        node.next = temp
        return dummy.next

    def oddEvenList(self, head):
        """
        Change given LL so that add odd indexed are in the front, followed by
        even indexed elements.
        """
        odd_head = ListNode(-1) # odd head
        odd = odd_head
        even_head = ListNode(-1) # even head
        even = even_head
        i = 1 # even vs odd tracker.
        while head != None:
            temp = head.next
            head.next = None
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            # move element and index
            head = temp
            i += 1
        # Finished separating, zip them together by adding even_head to odd.
        odd.next = even_head.next
        return odd_head.next

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
for (l, w) in [ ([[], []], []), ([[1,4,5], [2,3,6]], [1,2,3,4,5,6]), ([[2,3],[6],[1],[4],[5]], [1,2,3,4,5,6]) ]:
    heads = []
    for lst in l:
        heads.append(ll.fromList(lst))
    got = ll.mergeKLists(heads)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "mergekLists({}) = {}; want {}".format(heads, got, want)

############################### merge K lists on LL ##########################
for (l, v, w) in [ ([], 0, []), ([1], 1, []), ([1], 2, [1]), ([1,2,3], 2, [1,3]), ([1,1], 1, []) ]:
    head = ll.fromList(l)
    got = ll.remove(head, v)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "remove({}, {}) = {}; want {}".format(head, v, got, want)

############################### swap in pairs on LL ##########################
for (l, w) in [ ([], []), ([1], [1]), ([1,2], [2,1]), ([1,2,3], [2,1,3]), ([1,2,3,4], [2,1,4,3]) ]:
    head = ll.fromList(l)
    got = ll.swapInPairs(head)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "swapInPairs({}) = {}; want {}".format(head, got, want)

############################### rotate on LL ##########################
for (l, k, w) in [ ([], 0, []), ([1], 0, [1]), ([1,2], 1, [2,1]), ([1,2,3], 2, [2,3,1]), ([1,2,3,4], 4, [1,2,3,4]) ]:
    head = ll.fromList(l)
    got = ll.rotateRight(head, k)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "rotateRight({}, {}) = {}; want {}".format(head, k, got, want)

############################### remove on LL ##########################
for (l, v, w) in [ ([], 0, []), ([1], 1, []), ([1], 2, [1]), ([1,2,3], 2, [1,3]), ([1,1], 1, []) ]:
    head = ll.fromList(l)
    got = ll.remove(head, v)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "remove({}, {}) = {}; want {}".format(head, v, got, want)

############################### MIX on LL ##########################
for (l, w) in [ ([], []), ([1], [1]), ([1,2], [1,2]), ([1,2,3], [1,3,2]), ([1,2,3,4], [1,4,2,3]) ]:
    head = ll.fromList(l)
    got = ll.mix(head)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "mix({}) = {}, want {}".format(head, got, want)

############################### addTwoLL ##########################
for (l1, l2, w) in [ ([], [], []), ([1], [1], [2]), ([1], [1,2], [2,2]), \
                    ([9,9], [1], [0, 0, 1]), ([9,8,5], [1,1,5], [0,0,1,1]) ]:
    ll1 = ll.fromList(l1)
    ll2 = ll.fromList(l2)
    got = ll.addTwoLists(ll1, ll2)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "addTwoLists({}, {}) = {}, want {}".format(ll1, ll2, got, want)

for (l, w) in [ ([], []), ([1], [1]), ([1,2], [1,2]), ([3,2,1], [1,2,3]),\
                ([9,8,5], [5,8,9]) ]:
    lst = ll.fromList(l)
    got = ll.insertionSort(lst)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "insertionSort({}) = {}, want {}".format(l, got, want)

############################### oddEvenList Test ##########################
for (l, w) in [ ([], []), ([1], [1]), ([1,2], [1,2]), ([1,2,3], [1, 3, 2]), \
    ([1,2,3,4], [1,3,2,4]) ]:
    lst = ll.fromList(l)
    got = ll.oddEvenList(lst)
    want = ll.fromList(w)
    assert ll.equal(got, want), \
        "oddEvenList({}) = {}, want {}".format(lst, got, want)

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
