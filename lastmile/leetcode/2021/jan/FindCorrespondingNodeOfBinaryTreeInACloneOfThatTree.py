from TreeNode import TreeNode
import copy


class FindCorrespondingNodeOfBinaryTreeInACloneOfThatTree:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node=original
        stack=[]
        while node or stack:
            if node:
                stack.append((node, cloned))
                node=node.left
                cloned=cloned.left
            else:
                node,cloned=stack.pop()
                if node==target:
                    return cloned
                node=node.right
                cloned=cloned.right
        return None




if __name__ == '__main__':
    init = FindCorrespondingNodeOfBinaryTreeInACloneOfThatTree()
    root = TreeNode(7)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(19)

    clone=copy.deepcopy(root)
    print(init.getTargetCopy(root, clone, root.right))
