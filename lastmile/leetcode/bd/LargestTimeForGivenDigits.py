from typing import List


class LargestTimeForGivenDigits:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        self.max_time = []
        self.largestTimeFromDigitsInner(arr, [])
        return "" if not self.max_time else f"{self.max_time[0]}{self.max_time[1]}:{self.max_time[2]}{self.max_time[3]}"

    def largestTimeFromDigitsInner(self, arr, curr):
        if not arr:
            if (curr[0] * 10 + curr[1]) < 24 and int(curr[2] * 10 + curr[3]) < 60:
                #print(curr)
                self.max_time = max(curr, self.max_time)
                return

        for i in range(len(arr)):
            self.largestTimeFromDigitsInner(arr[:i]+arr[i+1:], curr+[arr[i]])

if __name__ == '__main__':
    init = LargestTimeForGivenDigits()
    #print(init.largestTimeFromDigits(arr = [1,2,3,4]))
    print(init.largestTimeFromDigits(arr = [0,0,1,0]))
