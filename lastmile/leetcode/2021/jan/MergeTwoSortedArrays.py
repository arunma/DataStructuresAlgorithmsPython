from typing import List


class MergeTwoSortedArrays:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[last] = nums1[m-1]
                last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                last -= 1
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

if __name__ == '__main__':
    init = MergeTwoSortedArrays()
    nums1 = [1, 2, 3, 0, 0, 0]
    print(init.merge(nums1, m = 3, nums2 = [2,5,6], n = 3))
    print (nums1)
    nums1=[1]
    print(init.merge(nums1, m = 1, nums2 = [], n = 0))
    print(nums1)

    nums1 = [0]
    print(init.merge(nums1, m=0, nums2=[1], n=1))
    print(nums1)
