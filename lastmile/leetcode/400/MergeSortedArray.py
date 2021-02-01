from typing import List


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[:n]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last=len(nums1)-1

        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1

        if n>0:
            nums1[:n]=nums2[:n]

if __name__ == '__main__':
    init = MergeSortedArray()
    nums1 = [1, 2, 3, 0, 0, 0]
    init.merge(nums1, m=3, nums2=[2, 5, 6], n=3) #[1,2,2,3,5,6]
    print(nums1)
