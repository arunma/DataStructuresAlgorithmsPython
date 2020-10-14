from typing import List


class MonotonicArray:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing=False
        decreasing=False

        for i in range(1, len(A)):
            if A[i-1]<A[i]:
                increasing=True
            elif A[i-1]>A[i]:
                decreasing=True

        if increasing and decreasing:
            return False
        return True

if __name__ == '__main__':
    init = MonotonicArray()
    print(init.isMonotonic([1,2,2,3])) #True
    print(init.isMonotonic([6,5,4,4])) #True
    print(init.isMonotonic([1,3,2])) #False
    print(init.isMonotonic([1,2,4,5])) #True
    print(init.isMonotonic([1,1,1])) #True
