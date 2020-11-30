from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for c in word:
            node=node.children[c]
        node.end=True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        if not word and node.end:
            return True
        elif not word and not node.end:
            return False

        if word[0]=='.':
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
        elif word[0] in node.children:
            return self.dfs(node.children[word[0]], word[1:])
        return False





if __name__ == '__main__':
    init = WordDictionary()
    init.addWord("bad")
    init.addWord("dad")
    init.addWord("mad")
    print(init.search("pad"))
    print(init.search("bad"))
    print(init.search(".ad"))
    print(init.search("b.."))
