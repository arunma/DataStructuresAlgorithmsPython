from typing import Optional

from leetcode.commons.TreeNode import TreeNode


class SerializeAndDeserializeBST:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        queue=[root]
        result=[str(root.val)]

        while queue:
            lcount=len(queue)
            for _ in range(lcount):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                result.append('#' if not node.left else str(node.left.val))

                if node.right:
                    queue.append(node.right)
                result.append('#' if not node.right else str(node.right.val))
        return ','.join(result)

    def deserialize(self, datastr: str) -> Optional[TreeNode]:
        data=datastr.split(',')
        root=TreeNode(data[0])
        index=1

        queue=[root]
        
        while queue:
            node=queue.pop(0)
            val=data[index]
            if val!='#':
                node.left=TreeNode(int(val))
                queue.append(node.left)
            index+=1

            val = data[index]
            if val!='#':
                node.right=TreeNode(int(val))
                queue.append(node.right)
            index+=1
        return root
                
            


if __name__ == '__main__':
    init = SerializeAndDeserializeBST()
    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(3)
    r2.right.left = TreeNode(4)
    r2.right.right = TreeNode(5)
    serial=init.serialize(r2)
    print(serial)
    print(init.deserialize(serial))
