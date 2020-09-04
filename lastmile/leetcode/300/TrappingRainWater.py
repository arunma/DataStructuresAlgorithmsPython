from typing import List


class TrappingRainWater:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left = 0
        right = len(heights) - 1
        maxleft = 0
        maxright = 0

        result = 0
        while left <= right:
            lheight = heights[left]
            rheight = heights[right]
            if lheight < rheight:
                if lheight > maxleft:
                    maxleft = lheight
                else:
                    result += maxleft - lheight
                left += 1
            else:
                if rheight > maxright:
                    maxright = rheight
                else:
                    result += maxright - rheight
                right -= 1

        return result


if __name__ == '__main__':
    init = TrappingRainWater()
    print(init.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
