
class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self) -> []:
       pass

class LeftMostColumnWithAtLeastAOne:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        r=0
        c=C-1

        leftMostCol=-1
        while r<R and c>=0:
            if binaryMatrix.get(r,c)==1:
                leftMostCol=c
                c-=1
            else:
                r+=1
        return leftMostCol

if __name__ == '__main__':
    init = LeftMostColumnWithAtLeastAOne()

