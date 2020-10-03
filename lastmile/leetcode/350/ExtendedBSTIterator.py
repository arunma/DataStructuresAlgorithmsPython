from TreeNode import TreeNode
class ExtendedBSTIterator:
    def __init__(self, root: TreeNode):
        self.stack=[]
        self.revstack=[]
        self.pushAll(root)


    def next(self) -> int:
        curr =None
        if self.stack:
            curr=self.stack.pop()
            self.pushAll(curr.right)
        self.revstack.append(curr)

        return curr.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node=node.left

    def hasPrev(self) -> bool:
        return self.revstack

    def prev(self) -> int:




if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    init = ExtendedBSTIterator(root)
    init.hasNext()  # true
    init.next()  # 3
    init.next()  # 7
    init.next()  # 9
    init.next()  # 15
    init.hasPrev()  # true
    init.prev()  # 9
    init.hasPrev()  # false bacause we can only move 1 step back
    init.next()  # 15
    init.next()  # 20
    init.hasNext()  # false
    init.hasPrev()  # true
    init.prev()  # 15
    init.hasNext()  # true
    init.next()  # 20


