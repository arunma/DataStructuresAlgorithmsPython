import sys
from typing import List


class SumOfSubarrayMinimums:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        ple = list(range(1, N + 1))
        nle = list(reversed(range(1, N + 1)))

        stack = []
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                stack.pop()
            if stack:
                ple[i] = i - stack[-1]
            else:
                ple[i] = i + 1
            stack.append(i)

        stack.clear()
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                topi = stack.pop()
                nle[topi] = i - topi
            stack.append(i)

        result = 0
        mod = 1_000_000_007

        for i, num in enumerate(arr):
            result = (result + num * ple[i] * nle[i]) % mod

        return result



if __name__ == '__main__':
    init = SumOfSubarrayMinimums()
    print(init.sumSubarrayMins([3, 1, 2, 4])) #17
    #print(init.sumSubarrayMins([3, 7, 8, 4]))
