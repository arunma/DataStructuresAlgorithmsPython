class MaxDifferenceChangingAnInteger:
    def maxDiff(self, num):
        numStr = str(num)
        i = 0
        while i < len(numStr) and numStr[i] == '9':
            i += 1

        a = numStr
        if i < len(numStr):
            a = numStr.replace(numStr[i], '9')

        j = 0
        b = numStr
        if numStr[j] == '1':
            while j < len(numStr) and (numStr[j] == '0' or numStr[j] == '1'):
                j += 1
            if j < len(numStr):
                b = numStr.replace(numStr[j], '0')

        else:
            b = numStr.replace(numStr[j], '1')

        return int(a) - int(b)


if __name__ == '__main__':
    init = MaxDifferenceChangingAnInteger()
    print(init.maxDiff(555))  # 888
    print(init.maxDiff(9))  # 9
    print(init.maxDiff(123456))  # 820000
    print(init.maxDiff(10000))  # 80000
    print(init.maxDiff(9288))  # 8700
    print(init.maxDiff(1101057))  # 8808050
