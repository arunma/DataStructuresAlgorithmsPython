class DeleteNode:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

if __name__ == '__main__':
    init = DeleteNode()
