from typing import List


class LongestSubarrayOf1AfterDeletingOneElement:
    def longestSubarray(self, nums: List[int]) -> int:
        ws = 0
        N = len(nums)
        zero_count = 0
        max_ones = -1
        for we in range(N):
            if nums[we] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[ws] == 0:
                    zero_count -= 1
                ws += 1
            max_ones = max(max_ones, we - ws)
        return max_ones


if __name__ == '__main__':
    init = LongestSubarrayOf1AfterDeletingOneElement()
    print(init.longestSubarray([1, 1, 0, 1]))  # 3
    print(init.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
    print(init.longestSubarray(nums=[1, 1, 1]))  # 2
    print(init.longestSubarray(nums=[0, 0, 0]))  # 0
