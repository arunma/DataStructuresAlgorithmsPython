from typing import List


class MaximumScoreOfSplicedArray:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)

        sum1=sum(nums1)
        sum2=sum(nums2)

        diff1=[]
        diff2=[]
        for i in range(N):
            diff1.append(nums1[i]-nums2[i])
            diff2.append(nums2[i]-nums1[i])

        max_sum1=0
        curr_max1=0

        for num in diff2:
            curr_max1=max(num, curr_max1+num)
            max_sum1=max(max_sum1, curr_max1)

        max_sum2=0
        curr_max2=0
        for num in diff1:
            curr_max2=max(num, curr_max2+num)
            max_sum2=max(max_sum2, curr_max2)

        return max(sum1+max_sum1, sum2+max_sum2)



if __name__ == '__main__':
    init = MaximumScoreOfSplicedArray()
    print(init.maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10])) #210
    #print(init.maximumsSplicedArray(nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]))#220
    #print(init.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1])) #31
