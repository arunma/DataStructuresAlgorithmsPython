from TreeNode import TreeNode


class SerializeAndDeserializeBinaryTree:
    def serialize(self, root):
        if not root: return
        queue=[]
        queue.append(root)
        result=[]
        while queue:
            node=queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)

            out=str(node.val) if node else '#'
            result.append(out)
        return ','.join(result)


    def deserialize(self, data):
        if not data: return

        nodes=data.split(",")
        index=1
        root = TreeNode(int(nodes[0]))
        queue=[]
        queue.append(root)

        while queue:
            node=queue.pop(0)
            if nodes[index]!='#':
                node.left=TreeNode(int(nodes[index]))
                queue.append(node.left)
            index+=1
            if nodes[index]!='#':
                node.right=TreeNode(int(nodes[index]))
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
    serial=init.serialize(r2)
    print(serial)
    print(init.deserialize(serial))
