from typing import List


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        N=len(candidates)
        self.bt(candidates, target, [], result, 0)
        return result

    def bt(self, candidates, target, currlist, result, start):
        if target<0:
            return
        if target==0:
            result.append(currlist.copy())
            return


        for i in range(start, len(candidates)):
            self.bt(candidates, target-candidates[i], currlist+[candidates[i]], result, i)


if __name__ == '__main__':
    init = CombinationSum()
    print(init.combinationSum([2, 3, 6, 7], target=7))
