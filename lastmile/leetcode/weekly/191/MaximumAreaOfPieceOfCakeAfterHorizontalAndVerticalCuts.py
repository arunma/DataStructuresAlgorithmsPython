from typing import List

# FIXME and try
class MaximumAreaOfPieceOfCakeAfterHorizontalAndVerticalCuts:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        dp = [[1] * w] * h

        for hh in horizontalCuts:
            for c in range(len(dp[0])):
                dp[hh - 1][c] = 0

        for vv in verticalCuts:
            for r in range(len(dp)):
                dp[r][vv - 1] = 0

        dp
        return -1


if __name__ == '__main__':
    init = MaximumAreaOfPieceOfCakeAfterHorizontalAndVerticalCuts()
    #print(init.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
    print(init.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
    # print(init.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
