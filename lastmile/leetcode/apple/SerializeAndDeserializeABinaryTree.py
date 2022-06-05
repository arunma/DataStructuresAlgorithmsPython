from collections import deque

from leetcode.commons.TreeNode import TreeNode

class SerializeAndDeserializeABinaryTree:
    def serialize(self, root):
        if not root:
            return ''
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node != '#':
                result.append(str(node.val))
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append('#')
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append('#')
            else:
                result.append('#')

        return ','.join(result)

    def deserialize(self, datas):
        if datas == '':
            return None

        data = datas.split(',')
        root = TreeNode(data[0])
        index = 1
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if data[index] != '#':
                node.left = TreeNode(data[index])
                queue.append(node.left)
            index += 1

            if data[index] != '#':
                node.right = TreeNode(data[index])
                queue.append(node.right)
            index += 1
        return root


if __name__ == '__main__':
    init = SerializeAndDeserializeABinaryTree()
    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(3)
    r2.right.left = TreeNode(4)
    r2.right.right = TreeNode(5)
    serial=init.serialize(r2)
    print(serial)
    print(init.deserialize(serial))

