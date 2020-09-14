class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.end=True


    def check(self, word):
        node=self.root
        for c in word:
            if c in node.children:
                node=node.children[c]
            else:
                return False
        return True if node.end else False

    def delete(self, word):
        node=self.root
        for c in word:
            if c in node.children:
                node=node.children[c]
            else:
                return False
        node.end=False
        return True

    def autoComplete(self, prefix):
        result=[]
        node=self.root
        for c in prefix:
           if c in node.children:
               node=node.children[c]
           else:
               return []

        self.bfs(node, prefix, result)
        return result

    def bfs(self, start, prefix, result):
        queue = []
        queue.append((start, prefix))
        while queue:
            node, prefix=queue.pop(0)
            if node.end:
                result.append(prefix)
            for k, nchild in node.children.items():
                queue.append((nchild, prefix+k))



if __name__ == '__main__':
    init = Trie()
    print(init.insert("hackerrank"))
    print(init.insert("hello"))
    print(init.check("hacker"))  # false
    print(init.check("hello"))  # true
    print(init.delete("hello"))  # true
    print(init.check("hello"))  # true
    print(init.insert("hacker"))
    print(init.autoComplete("hack"))
