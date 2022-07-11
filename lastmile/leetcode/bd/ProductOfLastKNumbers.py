class ProductOfLastKNumbers:

        def __init__(self):
            self.prefixprod = []
            self.prefixprod.append(1)

        def add(self, num: int) -> None:
            if num==0:
                self.prefixprod=[1]
            else:
                self.prefixprod.append(self.prefixprod[-1]*num)

        def getProduct(self, k: int) -> int:
            if k>=len(self.prefixprod):
                return 0
            beforek=self.prefixprod[-k-1]
            currprod=self.prefixprod[-1]
            return currprod/beforek


if __name__ == '__main__':
    init = ProductOfLastKNumbers()
    init.add(3)  # [3]
    init.add(0)  # [3,0]
    init.add(2)  # [3,0,2]
    init.add(5)  # [3,0,2,5]
    init.add(4)  # [3,0,2,5,4]
    print(init.getProduct(2))  # return 20. The product of the last 2 numbers is 5 * 4 = 20
    print(init.getProduct(3))  # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
    print(init.getProduct(4))  # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
    init.add(8)  # [3,0,2,5,4,8]
    print(init.getProduct(2))  # return 32. The product of the last 2 numbers is 4 * 8 = 32

