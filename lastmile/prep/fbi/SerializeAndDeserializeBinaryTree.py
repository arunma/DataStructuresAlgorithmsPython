from TreeNode import TreeNode


class SerializeAndDeserializeBinaryTree:

    def serialize(self, root):
        if not root:
            return ""

        queue=[root]

        result=[]
        while queue:
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)

            if not node:
                result.append("#")
            else:
                result.append(str(node.val))



        return ','.join(result)



    def deserialize(self, data):
        if not data:
            return

        snodes=data.split(",")
        root=TreeNode(snodes[0])

        queue=[root]
        index=1
        while queue:
            node=queue.pop(0)
            if snodes[index]!='#':
                node.left=TreeNode(snodes[index])
                queue.append(node.left)
            index+=1
            if snodes[index]!='#':
                node.right=TreeNode(snodes[index])
                queue.append(node.right)
            index+=1
        return root



if __name__ == '__main__':
    init = SerializeAndDeserializeBinaryTree()
    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(3)
    r2.right.left = TreeNode(4)
    r2.right.right = TreeNode(5)
    serial = init.serialize(r2)
    print(serial)
    print(init.deserialize(serial))
