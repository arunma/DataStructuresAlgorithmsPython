from typing import List


class SubsetsII:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     nums.sort()
    #     seen = set()
    #
    #     for mask in range(1 << n):
    #         subset = []
    #         for i in range(n):
    #             bit = (mask >> i) & 1  # Get i_th bit of mask
    #             if bit == 1:
    #                 subset.append(nums[i])
    #
    #         seen.add(tuple(subset))
    #
    #     return seen

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        N = len(nums)
        subsetnum = pow(2, N)

        for i in range(subsetnum):
            curr = []
            for j in range(N):
                if (i >> j) & 1:
                    curr.append(nums[j])
            result.add(tuple(curr))
        return result

if __name__ == '__main__':
    init = SubsetsII()
    print(init.subsetsWithDup([1, 2, 2])) #{(1, 2), (2,), (1,), (1, 2, 2), (2, 2), ()}
    print(init.subsetsWithDup([4,4,4,1,4])) #[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

