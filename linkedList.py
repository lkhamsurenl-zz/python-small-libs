# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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

################################ TEST   #############################
sol = Solution()
############################### reverse test ##########################
print("reverse LL test")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
rev = sol.reverse(head)
while rev != None:
    print(rev.val)
    rev = rev.next

############################### reverse test ##########################
print("Middle LL test")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
mid = sol.findMiddle(head)
assert(mid.val == 2)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)
mid = sol.findMiddle(head)
assert(mid.val == 2)
print("Middle LL tests passed!")

############################### Nth last test ##########################
print("Nth Last LL test")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
mid = sol.findNthLast(head, 1)
assert(mid.val == 3)
mid = sol.findNthLast(head, 2)
assert(mid.val == 2)
mid = sol.findNthLast(head, 3)
assert(mid.val == 1)

head = ListNode(1)
mid = sol.findNthLast(head, 1)
assert(mid.val == 1)

print("None case")
head = None
mid = sol.findNthLast(head, 1)
assert(mid.val == -1)
print("FindNthLast tests passed!")

############################### is Palindrome ##########################
print("LL palindrome test")
# only one element
head = ListNode(1)
assert(True == sol.isPalindrome(head))

# simple non palindrome odd case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
assert(False == sol.isPalindrome(head))

# even palindrome case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
assert(True == sol.isPalindrome(head))

# odd number of elements
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
assert(True == sol.isPalindrome(head))
print("isPalindrome LL tests passed!")
