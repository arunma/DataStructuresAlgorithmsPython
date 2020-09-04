def dfs(src, count, graph, start):
    while start != src:
        count += 1
        start = graph[start]
    return count


def findSignatureCounts(arr):
    graph = {}
    for i, a in enumerate(arr):
        graph[i+1] = a

    result = [0] * len(arr)
    for src in graph.keys():
        count = dfs(src, 1, graph, graph[src])
        result[src - 1] = count
    return result


if __name__ == '__main__':
    print(findSignatureCounts([2, 1]))
    print(findSignatureCounts([1, 2]))
    print(findSignatureCounts([4, 3, 2, 5, 1]))
