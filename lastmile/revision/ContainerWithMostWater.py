from typing import List


class ContainerWithMostWater:
    def maxArea(self, heights: List[int]) -> int:
        N=len(heights)
        if N<2:
            return 0
        left=0
        right=N-1
        max_area=0
        while left<right:
            lheight=heights[left]
            rheight=heights[right]
            diff=right-left

            curr_area=min(lheight, rheight)*diff
            max_area=max(max_area, curr_area)
            if lheight<rheight:
                left+=1
            else:
                right-=1

        return max_area








if __name__ == '__main__':
    init = ContainerWithMostWater()
    print(init.maxArea([1,8,6,2,5,4,8,3,7])) #49
    print(init.maxArea([1,1])) #1
