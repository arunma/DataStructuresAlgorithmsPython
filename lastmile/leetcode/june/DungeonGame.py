from typing import List

class DungeonGame:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        RI = len(dungeon) - 1
        CI = len(dungeon[0]) - 1
        dp = [[0] * len(dungeon[0]) for _ in range(len(dungeon))]

        for r in range(RI, -1, -1):
            for c in range(CI, -1, -1):
                if r == RI and c == CI:
                    dp[r][c] = min(0, dungeon[r][c])
                elif r == RI:
                    dp[r][c] = min(dp[r][c + 1] + dungeon[r][c], 0)
                elif c == CI:
                    dp[r][c] = min(dp[r + 1][c] + dungeon[r][c], 0)
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1]) + min(dungeon[r][c], 0)

        return abs(dp[0][0]) + 1


if __name__ == '__main__':
    init = DungeonGame()
    print(init.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]))
