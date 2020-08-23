class ReachingPoints:
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

if __name__ == '__main__':
    init = ReachingPoints()
    print(init.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5))
