import collections

from TreeNode import TreeNode


class BSTIterator:

    # def __init__(self, root: TreeNode):
    #     self.stack=[]
    #     self.pushAll(root)
    #
    # def pushAll(self, node):
    #     while node:
    #         self.stack.append(node)
    #         node=node.left
    #
    # def next(self) -> int:
    #     if self.stack:
    #         curr=self.stack.pop()
    #         self.pushAll(curr.right)
    #
    #     return curr.val
    #
    # def hasNext(self) -> bool:
    #     return True if self.stack else False

    def __init__(self, root: TreeNode):
        self.store = collections.deque()
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.store.appendleft(node.val)
                node = node.right

    def next(self) -> int:
        return self.store.pop()

    def hasNext(self) -> bool:
        return self.store


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    init = BSTIterator(root)
    print(init.next())  # return 3
    print(init.next())  # return 7
    print(init.hasNext())  # return true
    print(init.next())  # return 9
    print(init.hasNext())  # return true
    print(init.next())  # return 15
    print(init.hasNext())  # return true
    print(init.next())  # return 20
    print(init.hasNext())  # return false
