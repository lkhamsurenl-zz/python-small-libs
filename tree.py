from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        self.parent = None

class Tree(object):
    def treeEqual(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if not (root1 != None and root2 != None):
            return False
        return root1.val == root2.val and self.treeEqual(root1.left, root2.left) and \
                 self.treeEqual(root1.right, root2.right) 
    
    def height(self, root):
        """
        Find a height of the given tree.
        """
        if root == None:
            return -1
        return 1 + max(self.height(root.right), self.height(root.left))

    def maxPathSum(self, root):
        """
        Max path sum in a given tree.
        """
        return self.__recPathSum(root)[1]

    def __recPathSum(self, root):
        """
        return (maxPathSum in one side with root included, maxPathSum)
        """
        if root.left == None and root.right == None:
            return (root.val, root.val)
        (l, lm) = self.__recPathSum(root.left) if root.left != None else (0, -float('inf'))
        l = max(0, l) 
        (r, rm) = self.__recPathSum(root.right) if root.right != None else (0, -float('inf'))
        r = max(0, r)
        return (root.val + max(l, r), max(root.val + l + r, lm, rm))

    def inPostOrder(self, in_ord, post_ord):
        """
        Given a in and post order traversal of the tree in list, construct the tree
        """
        return self.__recInPost(in_ord, 0, len(in_ord) - 1, post_ord, 0, len(post_ord) - 1)

    def __recInPost(self, in_ord, in_start, in_end, post_ord, post_start, post_end):
        if in_start > in_end:
            return None # base case
        # Post order will visit the root as the last node.
        in_root = in_start
        while in_ord[in_root] != post_ord[post_end]:
            in_root += 1
        # Find end position of the left in post_ord.
        post_left_end = post_start + in_root - in_start - 1
        # Construct the root node.
        root = TreeNode(post_ord[post_end])
        root.left = self.__recInPost(in_ord, in_start, in_root - 1, post_ord, post_start, post_left_end)
        root.right = self.__recInPost(in_ord, in_root + 1, in_end, post_ord, post_left_end + 1, post_end - 1)
        return root

    def preInOrder(self, pre_ord, in_ord):
        """
        Given a pre and in order traversal of the tree in list, construct the tree
        """
        return self.__recPreIn(pre_ord, 0, len(pre_ord) - 1, in_ord, 0, len(in_ord) - 1)

    def __recPreIn(self, pre_ord, pre_start, pre_end, in_ord, in_start, in_end):
        if in_start > in_end:
            return None # base case
        # Pre order will visit the root as the first node.
        in_root = in_start
        while in_ord[in_root] != pre_ord[pre_start]:
            in_root += 1
        # Find end position of the left in pre_ord.
        pre_left_end = pre_start + in_root - in_start
        # Construct the root node.
        root = TreeNode(pre_ord[pre_start])
        root.left = self.__recPreIn(pre_ord, pre_start + 1, pre_left_end, in_ord, in_start, in_root - 1)
        root.right = self.__recPreIn(pre_ord, pre_left_end + 1, pre_end, in_ord, in_root + 1, in_end)
        return root

    def lowestCommonAncestor(self, root, node1, node2):
        """
        Given a tree with root, find a lowest common ancestor of node1 and node2
        """
        prefix = self.__commonPrefix__(self.__getEncoding__(root, node1),\
            self.__getEncoding__(root, node2))
        return self.__traverseEncoding__(root, prefix)
        
    def __getEncoding__(self, root, node):
        """
        Get encoding for node in root: 0 -> left, 1 -> right
        """
        if root == None:
            return "" # no valid encoding
        if root.left.val == node.val:
            return "0"
        if root.right.val == node.val:
            return "1" # right side encoded as 1
        l = self.__getEncoding__(root.left, node)
        if len(l) > 0:
            return "0" + l
        else:
            return "1" + self.__getEncoding__(root.right, node)

    def __commonPrefix__(self, encoding1, encoding2):
        i = 0
        while i < len(encoding1) and i < len(encoding2) and encoding1[i] == encoding2[i]:
            i += 1
        return encoding1[:i]

    def __traverseEncoding__(self, root, enc):
        """
        Given a encoding, follow it to get the node in that encoding.
        """
        node = root
        i = 0 
        while i < len(enc):
            node = root.left if enc[i] == "0" else root.right
            i += 1
        return node

class Codec:
    def ser(self, root):
        """
        Serializes a given tree in following way: [1,2,null, 3,4, null, null]
        """
        t = Tree()
        h = t.height(root) # find the height of the tree
        s = ["null"] * (2**(h + 1) - 1)
        self.__recSer(root, s, 0)
        return s
    def __recSer(self, root, s, i):
        if root == None:
            return 
        s[i] = root.val
        self.__recSer(root.left, s, 2 * i + 1)
        self.__recSer(root.right, s, 2 * i + 2)

    def deser(self, s):
        """
        constructs a tree from a serialized list: [1, 2, null] 
        """
        # length should be exactly 2^(h + 1) - 1 = len(s)
        return self.__recDeser(s,0)
    def __recDeser(self, s, i):
        if i >= len(s) or s[i] == 'null':
            return None
        root = TreeNode(s[i])
        root.left = self.__recDeser(s, 2 * i + 1)
        root.right = self.__recDeser(s, 2 * i + 2)
        return root

    def serialize(self, root):
        """
        Serializes the given TreeNode to [1, [2, [], []], [3, [], []]]
        """
        if root == None:
            return []
        return [root.val, self.serialize(root.left), self.serialize(root.right)]

    def deserialize(self, data):
        """
        deserializes the given data, which has the form:
        [1, [2, [], []], [3, [], []]]
        """
        if len(data) == 0:
            return None
        [ro, l, r] = data
        root = TreeNode(ro)
        root.left = self.deserialize(l)
        root.right = self.deserialize(r)
        return root

    def flatten(self, root):
        """
        Flatten the given tree to all the right pointers
        """
        if root == None or (root.left == None and root.right == None):
            return [root, root]
        [left_start, left_end] = self.flatten(root.left)
        [right_start, right_end] = self.flatten(root.right)
        # Connect the pointers
        root.left = None
        if left_start != None:
            root.right = left_start
            left_end.right = right_start
        # Find the end
        if right_end != None:
            end = right_end
        elif left_end != None:
            end = left_end
        else:
            end = root
        return [root, end]

class BST(object):
    def kthSmallest(self, root, k):
        """
        Find the kthSmallest element in the BST, using in-order traversal
        in-order traversal visit elements in BST smallest to largest order
        """
        if root == None:
            return -1 # no matching
        m = {} # node to index mapping, also indicate which elements has been visited
        index = 0 # current available index 
        stack = [root] # in-order traversal stack
        while len(stack) != 0:
            top = stack[-1] # top element
            if top.left != None and top.left not in m:
                stack.append(top.left)
            else:
                stack.pop() # remove the top element
                index += 1
                if index == k:
                    # we found the kth smallest element
                    return top.val
                m[top] = index
                if top.right != None:
                    stack.append(top.right)
        return -1 # k is out of bound

    

    def binarySearch(self, root, target):
        if root == None or root.val == target:
            return root
        if root.val < target:
            return self.binarySearch(root.right, target)
        else:
            return self.binarySearch(root.left, target)

    def lowestCommonAncestor(self, root, node1, node2):
        """
        Find the lowest common ancestor of valid nodes node1, node2 in BST
        """
        if root == None:
            return None # No valid common ancestor exist.
        if node1 == node2:
            return node1 # Nodes are same, so can safely return.
        # Make node1 always smaller than node2.
        if node1.val > node2.val:
            temp = node1
            node1 = node2
            node2 = temp
        if node1.val <= root.val <= node2.val:
            return root
        if node2.val < root.val:
            return self.lowestCommonAncestor(root.left, node1, node2)
        return self.lowestCommonAncestor(root.right, node1, node2)

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        (node, parent) = self.__searchNode__(root, key)
        if node == None:
                return root
        # node is leaf
        if node.right == None and node.left == None:
            if node == parent:
                return None # root.val == key and root is leaf
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return root
        
        # node has no right child
        if node.right == None:
            if node == parent:
                return node.left # root.val == key and root has no right child
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return root
        
        # node has right child
        current = node.right
        current_p = node
        while current.left != None:
            current_p = current
            current = current.left
        # found the closest node that is bigger in value than node
        node.val = current.val
        if current_p == node:
            node.right = current.right
        else:
            current_p.left = current.right
        
        return root

    def __searchNode__(self, root, key):
        current = root
        parent = root
        while current != None:
            if current.val == key:
                return (current, parent)
            parent = current
            if current.val < key:
                current = current.right
            else:
                current = current.left
        return (None, None)


class Traversal(object):
    """
    Pre, In, Level and Post order traversals in tree without using any recursion
    """
    def levelOrder(self, root):
        if root == None:
            return []
        ordering = []
        q = deque()
        q.appendleft(root)
        q.appendleft('#') # special symbol representing the current level
        while len(q) != 0:
            curr = q.pop()
            if curr == '#' and len(q) == 0:
                break
            elif curr == '#':
                q.appendleft('#') # put it back at the end representing level
            else:
                ordering.append(curr.val)
                if curr.left != None:
                    q.appendleft(curr.left)
                if curr.right != None:
                    q.appendleft(curr.right)
        return ordering

    def preOrder(self, root):
        ordering = []
        if root == None:
            return ordering
        s = [root]
        while len(s) != 0:
            top = s.pop()
            ordering.append(top.val)
            if top.right != None:
                s.append(top.right)
            if top.left != None:
                s.append(top.left)
        return ordering

    def inOrder(self, root):
        if root == None:
            return []
        s = [(root, 'NEW')] # each element has state associated with it
        ordering = []
        while len(s) != 0:
            (top, state) = s.pop()
            if top.left != None and state == 'NEW':
                s.append((top, 'VISITED')) # add the element back with new state
                s.append((top.left, 'NEW'))
            else: # done with the current element's left side
                ordering.append(top.val)
                if top.right != None:
                    s.append((top.right, 'NEW'))
        return ordering

    def postOrder(self, root):
        ordering = []
        if root == None:
            return ordering
        s = [(root, 'NEW')]
        while len(s) != 0:
            (top, state) = s.pop()
            if state == 'NEW':
                # Add the node back with changed state.
                s.append((top, 'DONE'))
                # Then add the right and left nodes, if possible.
                if top.right != None:
                    s.append((top.right, 'NEW'))
                if top.left != None:
                    s.append((top.left, 'NEW'))
            else:
                ordering.append(top.val)
        return ordering

    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = deque()
        queue.appendleft(root)
        queue.appendleft('#')
        lst = [[]]
        shouldBeReversed = False
        while len(queue) != 0:
            top = queue.pop() # right end element
            if top == '#' and len(queue) != 0:
                queue.appendleft(top)
                if shouldBeReversed:
                    lst[-1].reverse() # curr level si done, reverse it
                lst.append([]) # there is a new level starting
                shouldBeReversed = not shouldBeReversed
            elif top  != '#':
                lst[-1].append(top.val) # add to the last list
                if top.left is not None:
                    queue.appendleft(top.left) # add left side
                if top.right is not None:
                    queue.appendleft(top.right) # add right side
        # check for the last level, if it should be reversed
        if shouldBeReversed:
            lst[-1].reverse()
        return lst


#########                   TEST                #################
tree = Tree()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

#############               Serialize               ###################
codec = Codec()
ser = codec.serialize(root)
assert(ser == [1, [2, [], []], [3, [], []]])
deser = codec.deserialize(ser)
assert(tree.treeEqual(deser, root))
ser = codec.ser(root)
assert(ser == [1,2,3])
deser = codec.deser([1,2,3])
assert(tree.treeEqual(deser, root))

#############               BST Kth smallest                ###################
bst = BST()
root = codec.deserialize([7, [3, [1, [], []], [5, [], []]], [25, [10, [], []], []]])
for (target, want) in [(1,1), (2,3), (3,5), (4,7), (5, 10), (6, 25), (7, -1)]:
    got = bst.kthSmallest(root, target)
    assert got == want, \
        "kthSmallest(root, {}) = {}; want {}".format(target, got, want)

#############               Level Order             ###################
traversal = Traversal()
root = codec.deser([1,2,3,"null", 4, 5, "null"])
assert(traversal.levelOrder(root) == [1,2,3, 4, 5])
assert(traversal.inOrder(root) == [2, 4, 1, 5, 3])
assert(traversal.preOrder(root) == [1, 2, 4, 3, 5])
assert(traversal.postOrder(root) == [4,2, 5, 3,1])

###########                 In-Post Orders          #########################
for (i, p, w) in [ ([1], [1], [1]), ([1,2,3], [1,3,2], [2,1,3]), \
                     ([2,4,1,5,3], [4,2,5,3,1], [1,2,3,"null", 4, 5, "null"]) ]:
    got = tree.inPostOrder(i, p)
    want = codec.deser(w)
    assert tree.treeEqual(got, want), \
        "inPostOrder({}, {}) = {}; want {}".format(i, p, codec.ser(got), codec.ser(want)) 

###########                 Pre-In Orders           #########################
for (i, p, w) in [ ([1], [1], [1]), ([1,2,3], [2,1,3], [1,2,3]), \
                     ([1,2,4,3,5], [2,4,1,5,3], [1,2,3,"null", 4, 5, "null"]) ]:
    got = tree.preInOrder(i, p)
    want = codec.deser(w)
    assert tree.treeEqual(got, want), \
        "preInOrder({}, {}) = {}; want {}".format(i, p, codec.ser(got), codec.ser(want)) 

###########                 Lowest Common ancestor      ########################
# Test root is returned correctly when adding two elements on the two children.
t = codec.deser([1])
t.left = TreeNode(2)
t.right = TreeNode(3)
want = t
got = tree.lowestCommonAncestor(t, t.left, t.right)
assert got != None and got.val == want.val, \
        "lowestCommonAncestor({}) = {}; want {}".format(t, got.val, want.val) 
# Add two nodes on the left side of the tree.
t = codec.deser([1,2,3])
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
want = t.left
got = tree.lowestCommonAncestor(t, t.left.left, t.left.right)
assert got != None and got.val == want.val, \
        "lowestCommonAncestor({}) = {}; want {}".format(t, got.val, want.val) 

#############               BST remove node                 ###################
import copy
bst = BST()
t = Tree()
root = codec.deserialize([5, [3, [2, [], []], [4, [], []]], [6, [], [7, [], []]]])
# possible answers
root_removed_2 = codec.deserialize([5, [3, [], [4, [], []]], [6, [], [7, [], []]]])
root_removed_5 = codec.deserialize([6, [3, [2, [], []], [4, [], []]], [7, [], []]])
root_removed_3 = codec.deserialize([5, [4, [2, [], []], []], [6, [], [7, [], []]]])
for (key, want) in [(2, root_removed_2), (5, root_removed_5), (3, root_removed_3)]:
    got = bst.deleteNode(copy.deepcopy(root), key)
    assert t.treeEqual(got, want), \
        "deleteNode(root, {}) = {}; want {}".format(key, got, want)
