from leetcode.commons.TreeNode import TreeNode


class NumberOfGoodLeafNodePairs:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        self.dfs(root, distance)
        return self.result

    def dfs(self, root, distance):
        if not root:
            return []
        elif not root.left and not root.right:  # leaf
            return [1]

        lnodes = self.dfs(root.left, distance)
        rnodes = self.dfs(root.right, distance)

        for l in lnodes:
            for r in rnodes:
                if l + r <= distance:
                    self.result += 1

        #return [n + 1 for n in lnodes + rnodes if n + 1 < distance]
        ret = []
        for l in lnodes:
            if l+1<=distance:
                ret.append(l + 1)
        for r in rnodes:
            if r + 1 <= distance:
                ret.append(r + 1)

        return ret


if __name__ == '__main__':
    init = NumberOfGoodLeafNodePairs()
    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(3)
    r2.left.right = TreeNode(4)
    print(init.countPairs(r2, 3))
