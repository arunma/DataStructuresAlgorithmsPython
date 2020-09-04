import heapq


def findMaxProduct(arr):
    result = []
    max_pq=[]
    min_pq=[]

    for i, a in enumerate(arr):
        heapq.heappush(max_pq, -a)
        heapq.heappush(min_pq, a)
        if i < 2:
            result.append(-1)
        else:
            max1 = heapq.heappop(max_pq)
            max2 = heapq.heappop(max_pq)
            max3 = heapq.heappop(max_pq)
            pos_max=-max1 * -max2 * -max3
            heapq.heappush(max_pq, max1)
            heapq.heappush(max_pq, max2)
            heapq.heappush(max_pq, max3)

            min1 = heapq.heappop(min_pq)
            min2 = heapq.heappop(min_pq)
            neg_max=min1 * min2 * max1
            heapq.heappush(min_pq, min1)
            heapq.heappush(min_pq, min2)

            result.append(max(pos_max, neg_max))
    return result

if __name__ == '__main__':
    print(findMaxProduct([1, 2, 3, 4, 5]))
    print(findMaxProduct([2, 1, 2, 1, 2]))
