class MaskPII:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            atIdx = s.index('@')
            return "{}*****{}@{}".format(s[0].lower(), s[atIdx - 1].lower(), s[atIdx + 1:].lower())
        else:
            num_part = self.getNumeric(s)
            if len(num_part) >= 12:
                pre_ast = '*' * (len(num_part) - 10)
                return "+{}-***-***-{}".format(pre_ast, num_part[-4:])
            else:
                return "***-***-{}".format(num_part[-4:])

    def getNumeric(self, s: str):
        return ''.join([x for x in s if x not in "-+()"])


if __name__ == '__main__':
    init = MaskPII()
    print(init.maskPII("LeetCode@LeetCode.com")) #"l*****e@leetcode.com"
    print(init.maskPII("AB@qq.com")) #"a*****b@qq.com"
    print(init.maskPII("1(234)567-890")) #"***-***-7890"
    print(init.maskPII("86-(10)12345678")) #"+**-***-***-5678"
    print(init.maskPII("+86(88)1513-7-74")) #"+*-***-***-3774"
