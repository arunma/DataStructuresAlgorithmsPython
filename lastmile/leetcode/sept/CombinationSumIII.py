from typing import List


class CombinationSumIII:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        curr=[]
        self.helper(list(range(1, 10)), k, n, result, curr, 0)
        return result

    def helper(self, nums, k, target, result, curr, slot):
        if target==0 and len(curr)==k:
            result.append(curr.copy())
            return
        if target<0 or len(curr)>k:
            return

        for i in range(slot, len(nums)):
            curr.append(nums[i])
            self.helper(nums, k, target-nums[i], result, curr, i+1)
            curr.pop()



if __name__ == '__main__':
    init = CombinationSumIII()
    print(init.combinationSum3(k = 3, n = 7)) #[[1,2,4]]
    print(init.combinationSum3(k = 3, n = 9)) #[[1,2,6], [1,3,5], [2,3,4]]

