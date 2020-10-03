class AddStrings:
    def addStrings(self, num1: str, num2: str) -> str:
        lnum1 = list(num1)
        lnum2 = list(num2)

        carry = 0

        result = ''
        while lnum1 or lnum2 or carry:
            if lnum1:
                carry += int(lnum1.pop())
            if lnum2:
                carry += int(lnum2.pop())

            carry, value = divmod(carry, 10)
            result += str(value)

        return result[::-1]


if __name__ == '__main__':
    init = AddStrings()
    print(init.addStrings("98", "9"))
