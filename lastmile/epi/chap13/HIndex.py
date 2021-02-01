from typing import List


class HIndex:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, cit in enumerate(citations):
            if cit<i+1:
                return i
        return len(citations)


    def hIndexBucket(self, citations:List[int])-> int:
        N=len(citations)
        bucket=[0]*(N+1)
        for cit in citations:
            if cit>=N:
                bucket[N]+=1
            else:
                bucket[cit]+=1

        numcits=0
        for k in reversed(range(N+1)):
            numcits+=bucket[k]
            if numcits>=k:
                return k

        return 0



if __name__ == '__main__':
    init = HIndex()
    #print(init.hIndex([3,0,6,1,5]))
    #print(init.hIndexBucket([3,0,6,1,5]))
    #print(init.hIndexBucket([2,0,6,1,5]))
    #print(init.hIndexBucket([1,0,6,1,1]))
    #print(init.hIndexBucket([1,4,5,0,5]))
    print(init.hIndexBucket([5,4,3,0,5]))
