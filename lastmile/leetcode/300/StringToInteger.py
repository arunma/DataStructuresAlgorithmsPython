class StringToInteger:
    # def myAtoi(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     strip=list(s.strip())
    #     sign=-1 if strip[0]=='-' else 1
    #     if strip[0] in '-+':
    #         del strip[0]
    #
    #     if not strip[0].isdigit():
    #         return 0
    #
    #     num=0
    #     for c in strip:
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         else:
    #             break
    #
    #     retval=sign * num
    #     return max(-2147483648, min (retval, 2147483647))

    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        l = list(s.strip())

        if not l:
            return 0

        sign = -1 if l[0] == '-' else 1

        if l[0] in "+-":
            del l[0]

        num = 0

        for c in l:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break

        retval = sign * num

        return max(-2 ** 31, min(retval, 2 ** 31 - 1))


if __name__ == '__main__':
    init = StringToInteger()
    #print(init.myAtoi("42"))  # 42
    #print(init.myAtoi("   -42"))  # -42
    #print(init.myAtoi("4193 with words"))  # 4193
    #print(init.myAtoi("words and 987"))  # 0
    print(init.myAtoi("-91283472332"))  # -2147483648
    #print(init.myAtoi("3.14"))  # 3
