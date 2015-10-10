class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = ""
        self.children = {}
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # add symbol # to represent that it's the end of the word
        self.recIn(self.root, word + "#")
        
    def recIn(self, root, word):
        if len(word) == 0:
            return
        if word[0] in root.children:
            # recurse
            self.recIn(root.children[word[0]], word[1:])
        else:
            newChild = TrieNode()
            newChild.value = word[0]
            curr = newChild
            i = 1
            while i < len(word):
                child = TrieNode()
                child.value = word[i]
                curr.children[word[i]] = child
                curr = child
                i += 1
            root.children[word[0]] = newChild
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.recS(self.root, word + "#")
        
    def recS(self, root, word):
        if len(word) == 0:
            return True
        if word[0] in root.children:
            return self.recS(root.children[word[0]], word[1:])
        return False # have not found

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.recSW(self.root, prefix)
        
    def recSW(self, root, pre):
        if len(pre) == 0:
            return True
        if pre[0] in root.children:
            return self.recSW(root.children[pre[0]], pre[1:])
        return False

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("abcd")
assert(True == trie.search("abcd"))
assert(False == trie.search("abc"))
assert(True == trie.startsWith("ab"))
trie.insert("word")
assert(False == trie.search("worda"))
assert(True == trie.startsWith("word"))
assert(True == trie.search("word"))


