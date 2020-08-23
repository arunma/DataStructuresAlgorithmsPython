from typing import List


class CombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        curr=[]
        candidates.sort()
        self.combinationSum2Inner(candidates, target, result, curr, 0)
        return result

    def combinationSum2Inner(self, candidates, target, result, curr, start):
        if target<0:
            return
        if target==0:
            result.append(curr.copy())
        else:
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]: continue
                curr.append(candidates[i])
                self.combinationSum2Inner(candidates, target-candidates[i], result, curr, i+1)
                curr.pop()


if __name__ == '__main__':
    init = CombinationSumII()
    print(init.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    '''
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
    print(init.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
'''
[
  [1,2,2],
  [5]
]
'''
