class PreviousNextExperiments:
    def previous_next_element(self, nums):

        #nums = [float('-inf')] + nums + [float('-inf')]

        N = len(nums)
        #ple = list(range(1, N + 1))
        #nle = list(reversed(range(1, N + 1)))
        ple = [-1] * N
        nle = [-1] * N

        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1][0] > num:
                stack.pop()
            if stack:
                ple[i] = i - stack[-1][1]
            else:
                ple[i] = i + 1
            stack.append((num, i))
        print(ple)

        stack.clear()
        for i, num in enumerate(nums):
            while stack and stack[-1][0] > num:
                topnum, topi = stack.pop()
                nle[topi] = i - topi
            stack.append((num, i))
        print(nle)

        mod = 1_000_000_007
        sumresult = 0
        for i, (p, n) in enumerate(zip(ple, nle)):
            sumresult = (sumresult + nums[i] * p * n) %mod
        return sumresult

    def sumSubarrayMins(self, A):
        res = 0
        stack = []  # non-decreasing
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    init = PreviousNextExperiments()
    print(init.previous_next_element([2, 9, 7, 8, 3, 4, 6, 1]))
    print(init.previous_next_element([3, 1, 2, 4]))
    print(init.sumSubarrayMins([3, 1, 2, 4]))


[1, 1, 2, 1, 4, 1, 1, 8]
[7, 1, 2, 1, 3, 2, 1, 0]
109
[1, 2, 1, 1]
[1, 0, 0, 0]
3
17