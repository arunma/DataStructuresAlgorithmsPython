from typing import List


class MakeTwoArraysEqual:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target==arr

if __name__ == '__main__':
    init = MakeTwoArraysEqual()
    print(init.canBeEqual( target = [1,1,1,1,1], arr = [1,1,1,1,1]))
    print(init.canBeEqual( target = [1,2,3,4], arr = [2,4,1,3]))
    print(init.canBeEqual( target = [7], arr = [7]))
    print(init.canBeEqual( target = [3,7,9], arr = [3,7,11])) #false
