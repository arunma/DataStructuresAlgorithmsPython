class BeautifulArrangement:
    def countArrangement(self, n: int) -> int:
        if n==0:
            return 0

        self.res=0
        visited=[False]*(n+1)
        self.bt(visited, n, 1, [])
        return self.res

    def bt(self, visited, n, slot, curr):
        if slot>n:
            self.res+=1
            return
        for i in range(1, n+1):
            if visited[i]==False and (i % slot == 0 or slot % i == 0):
                visited[i]=True
                self.bt(visited, n, slot + 1, curr + [i])
                visited[i]=False

# 2
# 3
# 10
# 24679



if __name__ == '__main__':
    init = BeautifulArrangement()
    print(init.countArrangement(2))
    print(init.countArrangement(3))
    print(init.countArrangement(5))
    print(init.countArrangement(15))
