class IsRobotBounded:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [0, 1]
        curr = [0, 0]

        for inst in 4 * instructions:
            if inst == 'G':
                curr[0] += direction[0]
                curr[1] += direction[1]
            elif inst == 'L':
                direction = [-direction[1], direction[0]]
            elif inst == 'R':
                direction = [direction[1], -direction[0]]

        return True if curr == [0, 0] else False


if __name__ == '__main__':
    init = IsRobotBounded()
    print(init.isRobotBounded("GGLLGG"))
    print(init.isRobotBounded("GG"))
    print(init.isRobotBounded("GL"))
