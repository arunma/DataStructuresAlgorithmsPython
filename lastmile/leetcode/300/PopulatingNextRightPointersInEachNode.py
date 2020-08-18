class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class PopulatingNextRightPointersInEachNode:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue=[]
        dummy=Node()
        dummy.next=root
        queue.append(root)
        while queue:
            size=len(queue)
            prev=None
            for i in range(size):
                curr=queue.pop(0)
                if not prev:
                    prev=curr
                else:
                    prev.next=curr
                    prev=prev.next
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return dummy.next

if __name__ == '__main__':
    init = PopulatingNextRightPointersInEachNode()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(init.connect(root))
