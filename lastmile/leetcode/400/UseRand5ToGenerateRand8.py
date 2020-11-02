import random


class UseRand5ToGenerateRand8:
    # rand7() -> rand49() -> rand40() -> rand10()
    # rand5() -> rand25() -> rand24() -> rand8()
    def rand8(self):
        result = 24
        while result >= 24:
            result = (5 * self.rand5() - 1) + self.rand5() -1
        return result%8 +1

    def rand5(self):
        return random.randrange(1, 5)





if __name__ == '__main__':
    init = UseRand5ToGenerateRand8()
    print(init.rand8())


    # def rand10(self):
    #     result = 40
    #     while result >= 40:
    #         result = (7 * rand7()-1) + (rand7() - 1)
    #     return result % 10 + 1
    #
