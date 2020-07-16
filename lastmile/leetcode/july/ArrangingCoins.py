class ArrangingCoins:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n -= count
        return count if n == 0 else count - 1


if __name__ == '__main__':
    init = ArrangingCoins()
    print(init.arrangeCoins(5))
    print(init.arrangeCoins(8))
