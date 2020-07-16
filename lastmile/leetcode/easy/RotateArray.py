from typing import List


class RotateArray:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        self.reverse(nums, 0, N - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, N - 1)

    def reverse(self, nums, start, stop) -> None:
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start, stop = start + 1, stop - 1


if __name__ == '__main__':
    init = RotateArray()
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(init.rotate(nums, k=3))
    print(init.rotate(nums=[-1, -100, 3, 99], k=2))
    print(nums)
