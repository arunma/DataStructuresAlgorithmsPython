class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c not in node:
                    if c == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[c]
            return '$' in node

        return search_in_node(word, self.trie)


if __name__ == '__main__':
    init = WordDictionary()
    print(init.addWord("bad"))
    print(init.addWord("dad"))
    print(init.addWord("mad"))
    print(init.search("pad"))  # -> false
    print(init.search("bad"))  # -> true
    print(init.search(".ad"))  # -> true
    print(init.search("b.."))  # -> true
