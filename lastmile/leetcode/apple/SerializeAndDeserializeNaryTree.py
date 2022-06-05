# Definition for a Node.
from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class SerializeAndDeserializeNaryTree:

    def serialize(self, root: 'Node') -> str:
        if not root:
            return ''

        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()

            if node != '#':
                result.append(str(node.val))
                for child in node.children:
                    queue.append(child)
                queue.append("#")
            else:
                result.append('#')
        return ','.join(result)

    def deserialize(self, datas: str) -> 'Node':
        if datas == '':
            return None

        data = datas.split(',')
        root = Node(data[0], [])
        index = 1
        queue = deque([root])

        while queue:
            node = queue.popleft()
            while data[index] != '#':
                child = Node(data[index], [])
                node.children.append(child)
                queue.append(child)
                index += 1
            index += 1

        return root


if __name__ == '__main__':
    init = SerializeAndDeserializeNaryTree()
    rchild=[Node(3, [Node(5, []), Node(8, [])]),
            Node(2, [Node(9, [])]),
            Node(4,[Node(5, []), Node(6, []), Node(7, [])])]
    root=Node(1, rchild)
    print(init.serialize(root))


