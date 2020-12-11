from typing import List


class InsertInterval:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     result = []
    #     merged = newInterval
    #     for i, cinterval in enumerate(intervals):
    #         cstart, cend = cinterval
    #         if cend < merged[0]:
    #             result.append(cinterval)
    #         elif cstart > merged[1]:
    #             result.append(merged)
    #             return result + intervals[i:]
    #         else:
    #             merged[0] = min(merged[0], cstart)
    #             merged[1] = max(merged[1], cend)
    #
    #     result.append(merged)
    #     return result

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        nstart, nend = newInterval

        result = []

        for i, interval in enumerate(intervals):
            cstart, cend = interval

            if nend < cstart:
                result.append([nstart, nend])
                return result + intervals[i:]
            elif cend < nstart:
                result.append(interval)
            else:
                nstart = min(cstart, nstart)
                nend = max(cend, nend)
        result.append([nstart, nend])

        return result


if __name__ == '__main__':
    init = InsertInterval()
    print(init.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))  # Output: [[1,5],[6,9]]
    print(init.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1,2],[3,10],[12,16]])
