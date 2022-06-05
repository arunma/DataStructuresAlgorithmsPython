class IsHappyNumber:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            nextn = 0
            visited.add(n)
            while n != 0:
                n, v = divmod(n, 10)
                nextn += pow(v, 2)
            n = nextn

        return n == 1

if __name__ == '__main__':
    init = IsHappyNumber()
    print(init.isHappy(19))
    print(init.isHappy(3))
