# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
import bisect


class PreviousLessElement:
    def previous_less_element(self, A):
        ple_indices = [-1] * len(A)
        stack = []
        for i, num in enumerate(A):
            while stack and A[stack[-1]] > num:
                stack.pop()
            if stack:
                ple_indices[i] = stack[-1]
            stack.append(i)
        return ple_indices

    def next_less_element(self, A):
        stack = []
        next_less = [-1] * len(A)
        for i, num in enumerate(A):
            while stack and A[stack[-1]] > num:
                top = stack.pop()
                next_less[top] = i
            stack.append(i)
        return next_less

    def ple(self, nums):
        N=len(nums)
        stack=[]
        ple=[-1]*N

        for i, num in enumerate(nums):
            while stack and stack[-1]>num:
                stack.pop()
            if stack:
                ple[i]=stack[-1]
            stack.append(num)
        return ple

    def pge(self, nums):
        N=len(nums)
        stack=[]
        pge=[-1]*N

        for i, num in enumerate(nums):
            while stack and stack[-1]<num:
                stack.pop()
            if stack:
                pge[i]=stack[-1]
            stack.append(num)
        return pge

    def nle(self, nums):
        N=len(nums)
        stack=[]
        nle=[-1]*N

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]]>num:
                topi = stack.pop()
                nle[topi]=i
            stack.append(i)

        return [nums[i] if i!=-1 else 'x' for i in nle]

    def nge(self, nums):
        N=len(nums)
        stack=[]
        nle=[-1]*N

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                topi = stack.pop()
                nle[topi]=i
            stack.append(i)

        return [nums[i] if i!=-1 else 'x' for i in nle]


if __name__ == '__main__':
    init = PreviousLessElement()
    # print(init.previous_less_element([3, 7, 8, 4]))
    # print(init.previous_less_element_index([3, 7, 8, 4]))
    # print(init.find_ple([3, 7, 8, 4]))
    # print(init.previous_less_element([3, 7, 8, 4, 9]))
    # print(init.next_less_element([3, 7, 8, 4, 9]))
    # print(init.next_less_element([3, 1, 2, 4]))
    # print(init.previous_less_element([73, 74, 75, 71, 69, 72, 76, 73]))

    print(init.ple([3, 7, 8, 4, 9]))
    print(init.pge([3, 7, 8, 4, 9]))
    print(init.nle([3, 7, 8, 4, 9]))
    print(init.nge([3, 7, 8, 4, 9]))
