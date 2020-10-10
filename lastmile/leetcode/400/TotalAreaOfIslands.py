
class TotalAreaOfIslands:

    def totalAreaOfIsland(self, grid):
        sum=0
        for row in grid:
            sum+=row.count(1)
        return sum


if __name__ == '__main__':
    init = TotalAreaOfIslands()
    init = TotalAreaOfIslands()
    print(init.totalAreaOfIsland([[1, 1, 0, 0, 0],
                                  [1, 1, 0, 0, 0],
                                  [0, 0, 0, 1, 1],
                                  [0, 0, 0, 1, 1]]))
    print(init.totalAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
