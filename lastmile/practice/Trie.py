from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, ele: str):
        node = self.root
        for c in ele:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def check(self, search: str):
        node = self.root
        for ele in search:
            if node.children[ele]:
                node = node.children[ele]
            else:
                return False
        return node.end == True

    def delete (self, word: str):
        node=self.root
        for ele in word:
            if ele in node.children:
                node=node.children[ele]
        node.end=False
        return True




if __name__ == '__main__':
    init = Trie()
    print(init.insert("hackerrank"))
    print(init.insert("hello"))
    print(init.check("hacker"))  # false
    print(init.check("hello"))  # true
    print(init.delete("hello"))  # true
    print(init.check("hello"))  # true
# None
# None
# False
# True
# True
# False