class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        mapping={'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        N=len(s)
        result=0
        for i in range(N-1):
            if mapping[s[i+1]]<=mapping[s[i]]:
                result+=mapping[s[i]]
            else:
                result-=mapping[s[i]]
        result+=mapping[s[-1]]
        return result


if __name__ == '__main__':
    init = RomanToInteger()
    print(init.romanToInt('III'))
    print(init.romanToInt('IV'))
    print(init.romanToInt('VI'))
    print(init.romanToInt('LVIII')) #58
    print(init.romanToInt('MCMXCIV')) #1994
