from typing import List


class ContainerWithMostWater:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            lheight = heights[left]
            rheight = heights[right]

            curr_area = min(lheight, rheight) * (right - left)
            max_area=max(max_area, curr_area)

            if lheight<rheight:
                left+=1
            else:
                right-=1
        return max_area

if __name__ == '__main__':
    init = ContainerWithMostWater()
    print(init.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) #49
