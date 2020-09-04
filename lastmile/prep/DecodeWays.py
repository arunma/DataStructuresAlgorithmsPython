class DecodeWays:

    def numDecodings(self, digits):
        return self.numDecodingsInner(digits, 0)

    def numDecodingsInner(self, digits, slot):
        # if slot == len(digits) or slot == len(digits) - 1:
        #     return 1
        if slot == len(digits):
            return 1
        if digits[slot]=='0':
            return 0
        if slot == len(digits)-1:
            return 1

        count = self.numDecodingsInner(digits, slot + 1)
        if int(digits[slot:slot + 2]) <= 26:
            count += self.numDecodingsInner(digits, slot + 2)
        return count


if __name__ == '__main__':
    init = DecodeWays()
    # print(init.numDecodings("12"))  # 2
    # print(init.numDecodings("226"))  # 3
    print(init.numDecodings("13216"))  # 6
