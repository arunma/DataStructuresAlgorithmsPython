from collections import defaultdict


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['$']=True

    def search(self, word: str) -> bool:
        node=self.root
        for w in word:
            if w not in node:
                return False
            node=node[w]
        return '$' in node


    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for w in prefix:
            if w not in node:
                return False
            node=node[w]
        return True



if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.search("app"))  # returns true
