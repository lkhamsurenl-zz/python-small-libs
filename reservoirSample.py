
import random
class ListNode(object):
	def __init__(self, value):
		self.val = value
		self.next = None

def reservoirSampling(head, k):
	"""
	Given a large LL and number k, pick k elements uniformly random from the list
	The idea:
	First we pick first k elements
	For each element after that i, we pick random number between 1 to i
	If i correspond to the previously picked elements, then we replace with that indexed value with current
	Proof:
	suppose so far we've seen exactly N elements, therefore each element picked w/ Pr = k / N
	Now for element N + 1:
	Pr[N + 1 th picked] = Pr[Rand(1,N + 1) generate number in range 1 to k] = k / N + 1
	All other previously picked elements to survive, consider element @ index i:
	Pr[i survive for round N + 1] = Pr[(i survive N round) and (i not picked @ Rand(N + 1))] 
	Pr[i survive N round ] = k / N by induction  and Pr[i picked in Rand(N + 1)] = 1 / (N + 1)
	therefore Pr[i survive @ N + 1] = k / N *(1 - 1 / (N + 1)) = k / (N + 1), which proves all 
	elements are equally likely to be picked @ the end of the round N + 1, proving the induction
	step.
	"""
	count = 0
	sample = []
	while head != None and count < k:
		sample.append(head.val)
		head = head.next
		count += 1
	if head == None:
		return sample
	while head != None:
		i = random.randint(0, count)
		if i < k:
			sample[i] = head.val
		head = head.next
		count += 1
	return sample


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
for i in range(3):
	print(reservoirSampling(head, 1))
