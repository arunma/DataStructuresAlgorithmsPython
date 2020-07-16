from typing import List


class CanMakeArithmeticProgression:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr)<2:
            return True
        arr.sort()
        diff=arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] !=diff:
                return False
        return True

if __name__ == '__main__':
    init = CanMakeArithmeticProgression()
    print(init.canMakeArithmeticProgression([3,5,1]))
    print(init.canMakeArithmeticProgression([1,2,4]))
