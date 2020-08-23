from typing import List


class BestMeetingPoint:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])

        rows=[]
        cols=[]
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    rows.append(r)
                    cols.append(c)

        # rows.sort() Rows are already sorted
        cols.sort()
        medrow=rows[len(rows)//2]
        medcol=cols[len(cols)//2]

        distance=0
        for r in rows:
            distance+=abs(r-medrow)
        for c in cols:
            distance+=abs(c-medcol)

        return distance



if __name__ == '__main__':
    init = BestMeetingPoint()
    print(init.minTotalDistance([[1, 0, 0, 0, 1],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0]])) #6
