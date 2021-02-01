from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return

        N=len(nums)

        target=N-1
        while target>0:
            if nums[target-1]>nums[target]:
                target-=1
            else:
                break

        if target==0:
            nums.reverse()
            return

        target=target-1

        source=N-1
        while nums[source]<=nums[target]:
            source-=1

        nums[target],nums[source]=nums[source],nums[target]

        left=target+1
        right=N-1

        while left<=right:
            nums[left], nums[right]=nums[right],nums[left]
            left+=1
            right-=1


if __name__ == '__main__':
    init = NextPermutation()
    # x=[1, 2, 4, 3, 1]
    # init.nextPermutation(x) #[1,3,1,2,4]
    # print(x)
    # y=[1,2,3]
    # init.nextPermutation(y)
    # print (y) #[1,3,2]
    # z=[3,2,1]
    # init.nextPermutation(z)
    # print (z) #[1,2,3]
    a=[1,1]
    init.nextPermutation(a)
    print (a) #[1,2,3]
