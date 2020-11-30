from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.store={}
        for i, num in enumerate(nums):
            if num!=0:
                self.store[i]=num

    def dotProduct(self, vec: 'SparseVector') -> int:
        result=0
        for i, oth in vec.store.items():
            if i in self.store:
                result+=self.store[i] * oth
        return result




if __name__ == '__main__':
    vec1 = SparseVector([1,0,0,2,3])
    vec2 = SparseVector([0,3,0,4,0])
    print(vec1.dotProduct(vec2)) #8
