from typing import List


class CountingBits:

    # def countBits(self, num: int) -> List[int]:
    #     result = []
    #     result.append(0)
    #     for n in range(1, num + 1):
    #         result.append(self.count(n))
    #     return result
    #
    # def count(self, num: int):
    #     bits = 0
    #     while num != 0:
    #         bits = bits + (num & 1)
    #         num = num >> 1
    #     return bits
    def countBits(self, num: int) -> List[int]:
        result = []
        result.append(0)
        for n in range(1, num + 1):
            result.append(result[n >> 1] + (n & 1))
        return result

if __name__ == '__main__':
    init = CountingBits()
    print(init.countBits(2))  # [0,1,1]
    print(init.countBits(5))  # [0,1,1,2,1,2]
