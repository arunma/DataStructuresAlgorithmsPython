class CompareVersionNumbers:
    def compareVersion(self, version1: str, version2: str) -> int:

        iversion1 = [int(each) for each in version1.split(".")]
        iversion2 = [int(each) for each in version2.split(".")]

        N1 = len(iversion1)
        N2 = len(iversion2)

        if N1>N2:
            iversion2 += [0] * (N1 - N2)
        else:
            iversion1 += [0] * (N2 - N1)

        fversion1 = float(''.join(map(str, iversion1)))
        fversion2 = float(''.join(map(str, iversion2)))

        if fversion1 < fversion2:
            return -1
        elif fversion1 > fversion2:
            return 1
        else:
            return 0

if __name__ == '__main__':
    init = CompareVersionNumbers()
    print(init.compareVersion("0.1", "1.1")) #-1
    print(init.compareVersion("1.0.1", "1")) #1
    print(init.compareVersion("7.5.2.4", "7.5.3")) #-1
    print(init.compareVersion("1.01", "1.001")) #0
