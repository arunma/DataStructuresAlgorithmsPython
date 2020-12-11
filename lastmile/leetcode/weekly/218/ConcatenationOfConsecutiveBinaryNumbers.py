class ConcatenationOfConsecutiveBinaryNumbers:
    def concatenatedBinary(self, n: int) -> int:
        result=[]
        for i in range(1, n+1):
            result.append(bin(i)[2:])
        res= int(''.join(result), 2)
        return res % (pow(10, 9) +7)


if __name__ == '__main__':
    init = ConcatenationOfConsecutiveBinaryNumbers()
    print(init.concatenatedBinary(1)) #1
    print(init.concatenatedBinary(3)) #27
    print(init.concatenatedBinary(12)) #505379714
