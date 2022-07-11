from typing import List


class DailyTemperatures:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        N = len(temps)
        nge = [0] * N
        stack = []

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                top = stack.pop()
                nge[top] = i - top
            stack.append(i)
        return nge

if __name__ == '__main__':
    init = DailyTemperatures()
    print(init.dailyTemperatures([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]
    print(init.dailyTemperaturesPle([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]
