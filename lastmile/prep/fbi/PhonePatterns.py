class PhonePatterns:

    def generatePatterns(self, digits, charMap):
        result=[]
        curr=[]
        self.helper(digits, charMap, result, curr, 0)
        return result

    def helper(self, digits, charMap, result, curr, index):
        if index==len(digits):
            result.append(''.join(curr))
            return
        for i in range(index+1, len(digits)+1):
            subs=digits[index:i]
            if subs in charMap:
                for value in charMap[subs]:
                    curr.append(value)
                    self.helper(digits, charMap, result, curr, i)
                    curr.pop()


if __name__ == '__main__':
    init = PhonePatterns()
    charMap = {'1': ['A', 'B', 'C'],
               '2': ['D', 'E'],
               '12': ['X'],
               '3': ['P', 'Q']}
    print(init.generatePatterns("123", charMap))  # [ADP, ADQ, AEP, AEQ, BDP, BDQ, BEP, BEQ, CDP, CDQ, CEP, CEQ, XP, XQ]
