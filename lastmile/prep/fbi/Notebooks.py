def count(curr, adj):
    target=curr
    count=1
    while target!=adj[curr]:
        curr=adj[curr]
        count+=1
    return count

def findSignatureCounts(arr):
    adj_list={}

    for u,v in enumerate(arr):
        adj_list[u+1]=v

    result=[0]*len(arr)

    for curr in adj_list.keys():
        result[curr-1]=count(curr, adj_list)
    return result


if __name__ == '__main__':
    print(findSignatureCounts([2, 1])) #[2, 2]
    print(findSignatureCounts([1, 2])) #[1, 1]
    print(findSignatureCounts([4, 3, 2, 5, 1])) #[3, 2, 2, 3, 3]


