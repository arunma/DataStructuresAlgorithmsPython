from typing import List


class LexicographicalNumbers:
    # def lexicalOrder(self, n: int) -> List[int]:
    #     res = []
    #     cur = 1
    #     for _ in range(n):
    #         res.append(cur)
    #         if cur * 10 <= n:
    #             cur *= 10
    #         else:
    #             if cur >= n:
    #                 cur //= 10
    #             cur += 1
    #
    #             while cur % 10 == 0:
    #                 cur //= 10
    #     return res

    def lexicalOrder(self, n: int) -> List[int]:
        self.result=[]
        for i in range(1,10):
            self.dfs(i, n)

        return self.result

    def dfs(self, i, n):
        if i>n:
            return

        if i<=n:
            self.result.append(i)
            for d in range (10):
                if i*10+d>n:
                    break
                #print (i*10+d)
                self.dfs(i*10+d, n)




if __name__ == '__main__':
    init = LexicographicalNumbers()
    # print(init.lexicalOrder(1003))
    print(init.lexicalOrder(13))
    #print(init.lexicalOrder(103))
