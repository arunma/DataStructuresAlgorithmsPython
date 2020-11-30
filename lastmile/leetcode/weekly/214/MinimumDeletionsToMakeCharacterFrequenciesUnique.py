import heapq
from collections import Counter


class MinimumDeletionsToMakeCharacterFrequenciesUnique:
    def minDeletions(self, s: str) -> int:
        counter=Counter(s)

        pq=[]
        [heapq.heappush(pq, (-cnt, ch)) for ch,cnt in counter.items()]

        deletes=0
        while pq:
            cnt, ch= heapq.heappop(pq)
            if not pq:
                return deletes

            if cnt==pq[0][0]:
                cnt=-cnt
                if cnt>1:
                    heapq.heappush(pq, (-(cnt-1), ch))
                deletes+=1

        return deletes





        # deletions=0
        # freq=list(counter.keys())
        #
        # for i in freq:
        #     if i==0:
        #         break
        #     chars=counter[i]
        #
        #
        # for i, schar in enumerate(sset):
        #     if schar not in counter:
        #         cnt, ch = heapq.heappop(pq)
        #         result+= (-cnt)-i
        #     elif counter[i]>1:
        #         for






        # arr=list(counter.values())
        # arr.sort()
        #
        # result=0
        # for i in range(1, len(arr)):
        #     prev=arr[i-1]
        #     curr=arr[i]
        #
        #     if prev>=curr:
        #         result=prev-curr+1
        #         arr[i]=prev+1
        # return result



if __name__ == '__main__':
    init = MinimumDeletionsToMakeCharacterFrequenciesUnique()
    #print(init.minDeletions(s = "aab")) #0
    print(init.minDeletions(s = "aaabbbcc")) #2
    print(init.minDeletions(s = "ceabaacb")) #2
