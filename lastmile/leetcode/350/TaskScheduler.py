import heapq
from collections import Counter
from typing import List


class TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        pq=[]
        [heapq.heappush(pq, (-v, c)) for c,v in counter.items()]

        intervals=0
        while pq:
            k=n+1
            tempList=[]
            while k>0 and pq:
                intervals+=1
                k-=1
                tempList.append(heapq.heappop(pq))

            for v, c in tempList:
                v+=1 #Max heap. The value is negative. so, we are reducing the value
                if v<0:
                    heapq.heappush(pq, (v, c))
            if not pq:
                break
            intervals+=k
        return intervals



if __name__ == '__main__':
    init = TaskScheduler()
    print(init.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)) #8
    print(init.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0)) #6
    print(init.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)) #16
