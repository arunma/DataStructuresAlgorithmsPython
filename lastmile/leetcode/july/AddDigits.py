class AddDigits:
    def addDigits(self, num: int) -> int:
        result = 0
        while True:
            result += num % 10
            num //= 10
            if num == 0 and result <= 9:
                break
            elif num==0:
                num = result
                result=0

        return result


if __name__ == '__main__':
    init = AddDigits()
    print(init.addDigits(38))
