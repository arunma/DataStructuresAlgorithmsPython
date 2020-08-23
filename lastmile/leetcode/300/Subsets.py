from typing import List

#https://leetcode.com/problems/subsets/
class Subsets:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     curr = []
    #     result = [curr]
    #     for num in nums:
    #         for i in range(len(result)):
    #             result.append(result[i].copy()+[num])
    #     return result

    def subsetsBacktrack(self, nums: List[int]) -> List[List[int]]:
        result=[]
        curr=[]
        self.subsetsBackTrackInner(nums, result, curr, 0)
        return result

    def subsetsBackTrackInner(self, nums, result, curr, start):
        result.append(curr.copy())
        for i in range(start, len(nums)):
            curr.append(nums[i])
            #print ("i={}, s={}, curr={}".format(i, start, curr))
            self.subsetsBackTrackInner(nums, result, curr, i+1)
            curr.pop()




if __name__ == '__main__':
    init = Subsets()
    print(init.subsetsBacktrack([1, 2, 3]))
