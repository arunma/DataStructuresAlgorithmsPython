class FindPeakElement:

    # def findPeakElement(self, nums):
    #     N=len(nums)
    #     for i in range(N):
    #         if (i==0 or nums[i-1]<nums[i]) and (i==N-1 or nums[i]>nums[i+1]):
    #             return i
    #     return -1

    def findPeakElement(self, nums):
        N=len(nums)
        high=N-1
        low=0

        while low<=high:
            mid=low+(high-low)//2
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==N-1 or nums[mid]>nums[mid+1]):
                return mid

            if (mid==0 or nums[mid-1]<nums[mid]):
                low=mid+1
            else:
                high=mid-1
        return low




if __name__ == '__main__':
    init = FindPeakElement()
    print(init.findPeakElement([1, 2, 3, 1]))  # 2
    print(init.findPeakElement([1, 2, 5]))  #
    print(init.findPeakElement([5, 3, 2, 1]))  #
