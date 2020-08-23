from typing import List

# https://leetcode.com/problems/combination-sum/

class Combinationsum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        curr=[]
        self.combinationSumInner(candidates, curr, result, target, 0)
        return result

    def combinationSumInner(self, candidates, curr, result, target, start):
        if target<0:
            return
        if target==0:
            result.append(curr.copy())
        else:
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                self.combinationSumInner(candidates, curr, result, target-candidates[i], i)
                curr.pop()



if __name__ == '__main__':
    init = Combinationsum()
    print(init.combinationSum([2,3,6,7], target = 7))
