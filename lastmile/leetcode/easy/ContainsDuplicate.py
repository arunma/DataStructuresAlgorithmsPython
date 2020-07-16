from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

if __name__ == '__main__':
    init = ContainsDuplicate()
    print(init.containsDuplicate([1,2,3,1]))
