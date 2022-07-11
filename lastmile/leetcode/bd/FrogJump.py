from typing import List


class FrogJump:
    def canCross(self, stones: List[int]) -> bool:
        return self.canCrossInner(set(stones), 1, 0, stones[-1], set())

    def canCrossInner(self, stones, speed, curr, target, memo):
        if curr not in stones:
            return False

        if curr > target or speed <= 0 or curr < 0 or (curr, speed) in memo:
            return False

        if curr == target:
            return True

        nspeeds = [speed + 1, speed, speed - 1]

        for nspeed in nspeeds:
            if self.canCrossInner(stones, nspeed, curr + nspeed, target, memo):
                return True

        memo.add((curr, speed))
        return False


if __name__ == '__main__':
    init = FrogJump()
    #print(init.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # True
    #print(init.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # False
    print(init.canCross([0, 2]))  # False
