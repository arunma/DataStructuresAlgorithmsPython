from typing import List


class CampusBikes:

    def manhattanDistance(self, p1, p2) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes):
                distances.append((self.manhattanDistance(worker, bike), w, b))
        distances.sort()

        result = [-1] * len(workers)
        bikes_assigned = set()
        for distance, w, b in distances:
            if b in bikes_assigned:
                continue
            elif result[w]==-1:
                bikes_assigned.add(b)
                result[w] = b

        return result


if __name__ == '__main__':
    init = CampusBikes()
    print(init.assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
    print(init.assignBikes(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))
