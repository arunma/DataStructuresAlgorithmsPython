from typing import List


class FrogJump:
    # def canCross(self, stones: List[int]) -> bool:
    #     return self.canReach(set(stones), 1, 1, stones[-1])
    #
    #
    # def canReach(self, stones, curr, speed, target):
    #     if curr == target:
    #         return True
    #
    #     if speed<=0 or curr not in stones:
    #         return False
    #
    #     for j in (speed-1, speed, speed+1):
    #         #print(f"{curr}+{j}")
    #         if self.canReach(stones, curr+j, j, target):
    #             return True
    #     return False

    def canCross(self, stones: List[int]) -> bool:
        return self.dfs(set(stones), 1, 1, stones[-1], set())

    def dfs(self, stones, curr, speed, target, memo):
        print(f"curr :{curr}, speed: {speed}")
        if (curr, speed) in memo:
            print(f"curr :{curr}, speed: {speed} : False")
            return False

        if curr == target:
            print(f"curr :{curr}, speed: {speed} : True")
            return True

        if curr>target or curr<=0 or speed <=0 or curr not in stones:
            print(f"curr :{curr}, speed: {speed} : False")
            return False

        for s in [speed - 1, speed, speed + 1]:
            print(f"Iterating speed : {s}")
            if (curr+s) in stones:
                if self.dfs(stones, curr + s, s, target, memo):
                    return True

        memo.add((curr, speed))
        return False


if __name__ == '__main__':
    init = FrogJump()
    print(init.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # True
    #print(init.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # False

