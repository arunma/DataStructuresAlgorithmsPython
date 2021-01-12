class PartitioningIntoMinimumNumberOfDeciBinaryNumbers:
    def minPartitions(self, n: str) -> int:
        maxInt=0
        for e in n:
            maxInt=max(maxInt, int(e))
        return maxInt


if __name__ == '__main__':
    init = PartitioningIntoMinimumNumberOfDeciBinaryNumbers()
    print(init.minPartitions("32"))
    print(init.minPartitions("82734"))
    print(init.minPartitions("24322"))
