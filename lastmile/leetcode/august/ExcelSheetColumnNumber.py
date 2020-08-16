class ExcelSheetColumnNumber:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in s:
            curr = ord(c) - ord('A') + 1
            result = (result * 26) + curr
        return result


if __name__ == '__main__':
    init = ExcelSheetColumnNumber()
    print(init.titleToNumber("A"))  # 1
    print(init.titleToNumber("AB"))  # 28
    print(init.titleToNumber("ZY"))  # 701
