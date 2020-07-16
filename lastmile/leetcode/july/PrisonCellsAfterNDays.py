from typing import List


class PrisonCellsAfterNDays:
    # def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    #     K = len(cells)
    #     temp = [0] * K
    #     map={}
    #     for i in range(N):
    #         if str()
    #         for i in range(1, K-1):  # N-2
    #             prev = cells[i - 1]
    #             next = cells[i + 1]
    #             if prev == next:
    #                 temp[i] = 1
    #             else:
    #                 temp[i] = 0
    #         map[str(cells)]=temp
    #         cells=temp
    #     return cells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        K = len(cells)
        seen = {}
        while N:
            temp = [0] * K
            seen.setdefault(str(cells), N)
            N = N - 1
            for i in range(1, K - 1):  # N-2
                if cells[i - 1] == cells[i + 1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            cells = temp
            if str(cells) in seen:
                N = N % (seen[str(cells)] - N)

        return cells


if __name__ == '__main__':
    init = PrisonCellsAfterNDays()
    print(init.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))  # [0, 0, 1, 1, 0, 0, 0, 0]
    print(init.prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))  # [0,0,1,1,1,1,1,0]
