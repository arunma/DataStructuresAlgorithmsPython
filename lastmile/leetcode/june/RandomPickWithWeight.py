import random as rand


class Solution:
    def __init__(self, w):
        self.cumulative_sum = []
        self.total = 0
        sumw = 0
        for i in w:
            sumw = sumw + i
            self.cumulative_sum.append(sumw)
        self.total = self.cumulative_sum[-1]

    def pickIndex(self):
        rand_val = rand.randint(1, self.total)
        index = self.binary_search(self.cumulative_sum, rand_val, 0, len(self.cumulative_sum) - 1)
        return index

    def binary_search(self, cumulative_sum, rand_val, low, high):
        while low <= high:
            mid = (low + high) // 2
            if cumulative_sum[mid] == rand_val:
                return mid
            elif cumulative_sum[mid] < rand_val:
                low = mid + 1
            elif cumulative_sum[mid] > rand_val:
                high = mid - 1

        return low


if __name__ == '__main__':
    init = Solution([1, 3])
    print(init.pickIndex())
    print(init.pickIndex())
    print(init.pickIndex())
    print(init.pickIndex())
    print(init.pickIndex())
    print()
    init = Solution([1])
    print(init.pickIndex())
