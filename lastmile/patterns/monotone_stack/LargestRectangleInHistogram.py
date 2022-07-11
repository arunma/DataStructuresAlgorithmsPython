import sys
from typing import List


class LargestRectangleInHistogram:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxrect = 0
        heights = heights + [-1]

        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                topi = stack.pop()
                top = heights[topi]

                width = i if not stack else i - stack[-1] - 1
                currmax = top * width

                maxrect = max(maxrect, currmax)
            stack.append(i)
        return maxrect


if __name__ == '__main__':
    init = LargestRectangleInHistogram()
    print(init.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(init.largestRectangleArea([1, 1]))  # 2
    print(init.largestRectangleArea([2, 4]))  # 4
    print(init.largestRectangleArea([2, 1, 2]))  # 3
    print(init.largestRectangleArea([1, 1, 1, 6, 2]))  # 6
