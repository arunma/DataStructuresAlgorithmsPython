from typing import List


class ShuffleAnArray:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        for x,y in zip(nums[0:n], nums[n:len(nums)]):
            result.append(x)
            result.append(y)
        return result

if __name__ == '__main__':
    init = ShuffleAnArray()
    print(init.shuffle([2,5,1,3,4,7], 3))
