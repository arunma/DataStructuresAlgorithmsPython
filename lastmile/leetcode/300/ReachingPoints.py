class ReachingPoints:
    # def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    #     if sx == tx and sy == ty:
    #         return True
    #     if sx > tx or sy > ty:
    #         return False
    #     else:
    #         return self.reachingPoints(sx, sx + sy, tx, ty) or self.reachingPoints(sx + sy, sy, tx, ty)
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        memo={}
        return self.search(sx, sy, tx, ty, memo)

    def search(self, sx: int, sy: int, tx: int, ty: int, memo) -> bool:
        if ((sx, sy)) in memo:
            return memo[(sx, sy)]
        if sx==tx and sy==ty:
            memo[(sx, sy)]=True
            return True
        elif sx>tx or sy>ty:
            memo[(sx, sy)] = False
            return False
        else:
            return self.search(sx, sx+sy, tx, ty, memo) or self.search(sx+sy, sy, tx, ty, memo)

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        memo = {}
        return self.reachingPointsHelper(sx, sy, tx, ty, memo)

    def reachingPointsHelper(self, sx: int, sy: int, tx: int, ty: int, memo) -> bool:
        if (sx, sy) in memo:
            return memo[(sx, sy)]

        if sx == tx and sy == ty:
            memo[(sx, sy)] = True
            return True
        elif sx > tx or sy > ty:
            memo[(sx, sy)] = False
            return False
        else:
            return self.reachingPointsHelper(sx, sx + sy, tx, ty, memo) or self.reachingPointsHelper(sx + sy, sy, tx,
                                                                                                     ty, memo)


if __name__ == '__main__':
    init = ReachingPoints()
    print(init.reachingPoints(sx=1, sy=1, tx=3, ty=5))  # True
    print(init.reachingPoints(sx=9, sy=5, tx=12, ty=8))  # False
    print(init.reachingPoints(3, 3, 12, 9) )  # True
