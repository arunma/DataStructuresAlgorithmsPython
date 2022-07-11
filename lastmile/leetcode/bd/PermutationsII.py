from typing import List


class PermutationsII:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     self.result = []
    #     self.permuteInner(nums, [])
    #     return self.result
    #
    # def permuteInner(self, nums, curr):
    #     if not nums:
    #         self.result.append(curr.copy())
    #
    #     for i in range(len(nums)):
    #         if i > 0 and nums[i - 1] == nums[i]:
    #             continue
    #         self.permuteInner(nums[:i] + nums[i + 1:], curr + [nums[i]])


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result=[]
        self.visited=[False]*len(nums)
        self.permuteInner(nums, [])
        print(len(self.result))
        return self.result

    def permuteInner(self, nums, curr):
        if len(curr)== len(nums):
            self.result.append(curr.copy())
            return

        for i in range(len(nums)):
            #if self.visited[i] or (i>0 and nums[i]==nums[i-1] and self.visited[i-1]):
            #    continue

            if self.visited[i]:
                continue

            self.visited[i]=True
            print("Forward +++++++ ", self.visited)
            print("curr+nums[i] --->", curr+[nums[i]])
            self.permuteInner(nums, curr+[nums[i]])
            self.visited[i] = False
            print("Reverse ------- ", self.visited)



if __name__ == '__main__':
    init = PermutationsII()
    #print(init.permuteUnique([1,1,2]))
    print(init.permuteUnique([1,2,3]))
