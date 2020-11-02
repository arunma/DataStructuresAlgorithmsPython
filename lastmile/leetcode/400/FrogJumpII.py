from collections import defaultdict


class FrogJumpII:
    def canCross(self, stones):
        if not stones:
            return True

        N = len(stones)
        steps = defaultdict(set)
        steps[0].add(1)

        for i, stone in enumerate(stones):
            for step in steps[stone]:
                reach = step + stone
                if reach == stones[-1]:
                    return True

                steps[reach].add(step)
                if step - 1 > 0: steps[reach].add(step - 1)
                steps[reach].add(step + 1)

        return False


if __name__ == '__main__':
    init = FrogJumpII()
    print(init.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # True
    print(init.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # False
