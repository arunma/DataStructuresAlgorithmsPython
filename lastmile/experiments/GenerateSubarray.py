import bisect


class GenerateSubarray:

    def generateSubarray(self, nums):
        N=len(nums)
        result=[]
        for i in range(N+1):
            for j in range(i+1, N+1):
                result.append(nums[i:j])
        return result

if __name__ == '__main__':
    init = GenerateSubarray()
    nums=[1, 2, 3, 4]
    N=len(nums)
    result=init.generateSubarray(nums)
    print(result)
    assert (len(result)==(N*(N+1)//2))

    #Total number of subarrays with 3
    three_left=nums.index(3)+1
    three_right=N-three_left+1
    print(three_left*three_right)

    three_count=0
    for each in result:
        if 3 in each:
            three_count+=1
    assert(three_count==(three_left*three_right))

