import sys
from typing import List


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)

        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = N1

        while low <= high:
            mx = (low+high) // 2
            my = (N1 + N2 + 1)//2 - mx

            leftXVal = -sys.maxsize if mx==0 else nums1[mx-1]
            leftYVal = -sys.maxsize if my==0 else nums2[my-1]

            rightXVal = sys.maxsize if mx==N1 else nums1[mx]
            rightYVal = sys.maxsize if my==N2 else nums2[my]

            if leftXVal<=rightYVal and leftYVal<=rightXVal:
                if (N1+N2)%2==0:
                    return (max(leftXVal, leftYVal)+min(rightXVal, rightYVal))/2.0
                else:
                    return max(leftXVal,leftYVal)
            if leftXVal>rightYVal:
                high=mx-1
            elif rightXVal<leftYVal:
                low=mx+1
        return -1

if __name__ == '__main__':
    init = MedianOfTwoSortedArrays()
    print(init.findMedianSortedArrays([1, 2, 5], [4, 6, 7]))
    print(init.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(init.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
