from typing import List


class IntervalListIntersection:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i=j=0
        m=len(A)
        n=len(B)

        result=[]
        while i<m and j<n:
            astart, aend=A[i]
            bstart, bend=B[j]

            if astart<=bend and bstart<=aend:
                result.append([max(astart, bstart), min(aend, bend)])

            if aend<=bend:
                i+=1
            else:
                j+=1

        return result




if __name__ == '__main__':
    init = IntervalListIntersection()
    print(init.intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                    B=[[1, 5], [8, 12], [15, 24],
                                       [25, 26]]))  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
