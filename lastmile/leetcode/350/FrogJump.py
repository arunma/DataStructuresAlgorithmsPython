from typing import List


class FrogJump:
    # def canCross(self, stones):
    #     target=stones[-1]
    #     curr=1
    #     speed=1
    #     return self.canCrossHelper(stones, curr, speed, target)
    #
    # def canCrossHelper(self, stones, curr, speed, target):
    #     if curr==target:
    #         return True
    #
    #     if speed<=0 or curr not in stones:
    #         return False
    #
    #     speeds=[speed + 1, speed, speed - 1]
    #     for sp in speeds:
    #             if self.canCrossHelper(stones, curr + sp, sp, target):
    #                 return True
    #     return False

    def canCross(self, stones):
        target = stones[-1]
        curr = 1
        speed = 1
        memo = set()
        return self.canCrossHelperBt(set(stones), curr, speed, target, memo)

    def canCrossHelperBt(self, stones, curr, speed, target, memo):
        if (curr, speed) in memo:
            return False
        if curr == target:
            return True

        if speed <= 0 or curr not in stones:
            return False

        for j in (speed - 1, speed, speed + 1):
            if self.canCrossHelperBt(stones, curr + j, j, target, memo):
                return True

        memo.add((curr, speed))
        return False


if __name__ == '__main__':
    init = FrogJump()
    print(init.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # True
    print(init.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # False
