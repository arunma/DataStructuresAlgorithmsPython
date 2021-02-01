class ConcatenationOfConsecutiveBinaryNumbers:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        #MOD = 10**9 + 7
        MOD=1000000007
        for curr in range(1, n + 1):
            lencurr=(len(bin(curr)) - 2)
            result = ((result << lencurr) + curr) % MOD

        return result


if __name__ == '__main__':
    init = ConcatenationOfConsecutiveBinaryNumbers()
    print(init.concatenatedBinary(1))  # 1
    print(init.concatenatedBinary(3))  # 27
    print(init.concatenatedBinary(12))  # 505379714
