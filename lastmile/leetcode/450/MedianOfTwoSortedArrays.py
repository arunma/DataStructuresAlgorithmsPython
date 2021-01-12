from typing import List


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m = len(A)
        n = len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        if n == 0:
            raise ValueError

        l = 0
        r = m

        while l <= r:
            i = (l + r) // 2
            j = ((m + n + 1) // 2) - i

            if i < m and B[j - 1] > A[i]:
                l = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                r = i - 1
            else:
                if i == 0:
                    maxLeft = B[j - 1]
                elif j == 0:
                    maxLeft = A[i - 1]
                else:
                    maxLeft = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return maxLeft

                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(A[i], B[j])

                return (minRight + maxLeft) / 2.0
        return 0.0


if __name__ == '__main__':
    init = MedianOfTwoSortedArrays()
    print(init.findMedianSortedArrays(A=[1, 2, 5], B=[4, 6, 7]))
    # init.findMedianSortedArrays(nums1=[1, 3], nums2=[2])
    # init.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
