from typing import List


class PermutationsII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        curr=[]
        self.permuteUniqueInner(nums, result, curr)
        return result

    def permuteUniqueInner(self, nums, result, curr):
        if not nums:
            result.append(curr.copy())
            return
        else:
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]: continue
                #curr.append(nums[i])
                self.permuteUniqueInner(nums[:i]+nums[i+1:], result, curr+[nums[i]])
                #curr.pop()


if __name__ == '__main__':
    init = PermutationsII()
    print(init.permuteUnique([1,1,2]))
