from typing import List


class SubsetsBit:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        subsetnum=pow(2,N)

        result=[]
        for j in range(subsetnum):
            curr = []
            for i in range(N):
                if (j>>i)&1:
                    curr.append(nums[i])
            result.append(curr.copy())
        return result



if __name__ == '__main__':
    init = SubsetsBit()
    print(init.subsets(nums=[1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(init.subsets(nums=[0]))  # [[],[0]]
