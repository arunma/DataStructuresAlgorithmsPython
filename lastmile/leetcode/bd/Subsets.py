from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        self.bt(nums, [], 0)
        return self.result

    def bt(self, nums, curr, index):
        if index>len(nums):
            return
        self.result.append(curr.copy())

        for i in range(index, len(nums)):
            self.bt(nums, curr+[nums[i]], i+1)



if __name__ == '__main__':
    init = Subsets()
    print(init.subsets(nums = [1,2,3])) #[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(init.subsets(nums = [0])) # [[],[0]]


