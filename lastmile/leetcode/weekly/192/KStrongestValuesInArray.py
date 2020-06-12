import functools
from typing import List


class KStrongestValuesInArray:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        med_index = (len(arr) - 1) // 2
        median = arr[med_index]

        def strongest_compare(x, y):
            a = abs(x - median)
            b = abs(y - median)
            if a == b:
                return 1 if x > y else -1
            elif a > b:
                return 1
            return -1

        arr.sort(key=functools.cmp_to_key(strongest_compare), reverse=True)
        return arr[:k]

if __name__ == '__main__':
    init = KStrongestValuesInArray()
    print(init.getStrongest([1, 2, 3, 4, 5], k=2))  # [5,1]
    print(init.getStrongest(arr=[1, 1, 3, 5, 5], k=2))  # [5,5]
    print(init.getStrongest([6, -3, 7, 2, 11], k=3))  # [-3,11,2]
    print(init.getStrongest(arr=[-7, 22, 17, 3], k=2))  # 22,17
