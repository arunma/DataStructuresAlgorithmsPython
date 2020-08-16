class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}". format(int(a, 2) + int(b, 2))

if __name__ == '__main__':
    init = AddBinary()
    print(init.addBinary(a = "11", b = "1")) #100
    print(init.addBinary(a = "1010", b = "1011")) #10101
