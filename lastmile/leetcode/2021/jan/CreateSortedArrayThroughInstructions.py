from typing import List

#Fenwick tree
class CreateSortedArrayThroughInstructions:
    def createSortedArray(self, instructions: List[int]) -> int:
        N=max(instructions)
        c=[0] * (N+1)
        mod=10**9 +7

        def update(x):
            while x<=N:
                c[x]+=1
                x+= x & -x

        def get(x):
            ans=0
            while x>0:
                ans+=c[x]
                x-= x&-x
            return ans

        result=0
        for i, num in enumerate(instructions):
            left=get(num-1)
            right=i-get(num)
            result+=min(left, right)
            update(num)
        return result%mod


if __name__ == '__main__':
    init = CreateSortedArrayThroughInstructions()
    print(init.createSortedArray([1,2,3,6,5,4])) #3
    print(init.createSortedArray([1,5,6,2]))#1
    print(init.createSortedArray([4,14,10,2,5,3,8,19,7,20,12,1,9,15,13,11,18,6,16,17]))#43
