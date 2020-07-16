class KthFactorOfN:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
            if count == k:
                return i

        return -1


if __name__ == '__main__':
    init = KthFactorOfN()
    print(init.kthFactor(n=12, k=3))  # 3
    print(init.kthFactor(n=1000, k=3))  # 4
    print(init.kthFactor(n=4, k=4))  # -1
    print(init.kthFactor(n=1, k=1))  # 1
