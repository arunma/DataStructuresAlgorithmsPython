from typing import List

# class CmpKey(str):
#     def __lt__(x,y):
#         return x+y > y+x
#
# class LargestNumber:
#     def largestNumber(self, nums: List[int]) -> str:
#         order=sorted(map(str, nums), key=CmpKey)
#         return ''.join(order)

class Cmp(str):
    def __lt__(this, that):
        return this+that > that+this

class LargestNumber:
    def largestNumber(self, arr):
        strs=[str(i) for i in arr]
        strs.sort(key=Cmp)
        return ''.join(strs).lstrip('0') or '0'

if __name__ == '__main__':
    init = LargestNumber()
    print(init.largestNumber([10,2])) #210
    print(init.largestNumber([3,30,34,5,9])) #9534330
    print(init.largestNumber([0,0])) #9534330
