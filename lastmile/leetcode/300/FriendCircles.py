from typing import List


class FriendCircles:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N=len(M)
        visited=[False]*N
        count=0
        for person in range(N):
                if not visited[person]:
                    self.visitFriends(M, visited, person)
                    count += 1
        return count

    def visitFriends(self, M, visited, person):
        visited[person] = True
        for friend in range(len(M)):
            if not visited[friend] and M[person][friend]==1:
                self.visitFriends(M, visited, friend)

    # def findCircleNum(self, A):
    #     N = len(A)
    #     seen = set()
    #
    #     def dfs(node):
    #         for nei, adj in enumerate(A[node]):
    #             if adj and nei not in seen:
    #                 seen.add(nei)
    #                 dfs(nei)
    #
    #     ans = 0
    #
    #     for i in range(N):
    #         if i not in seen:
    #             dfs(i)
    #             ans += 1
    #     return ans

if __name__ == '__main__':
    init = FriendCircles()
    grid3 = [[1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 0, 1, 1]]
    print(init.findCircleNum(grid3))
