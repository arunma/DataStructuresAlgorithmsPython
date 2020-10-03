from typing import List


class CarPooling:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripPass=[]
        for nump, start, end in trips:
            tripPass.append((start,nump))
            tripPass.append((end, -nump))

        tripPass.sort()

        ccap=0
        for pos, nump in tripPass:
            ccap+=nump
            if ccap>capacity:
                return False
        return True


if __name__ == '__main__':
    init = CarPooling()
    print(init.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))  # false
    print(init.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))  # true
    print(init.carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))  # true
    print(init.carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))  # true
