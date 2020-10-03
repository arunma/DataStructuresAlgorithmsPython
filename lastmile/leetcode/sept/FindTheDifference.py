class FindTheDifference:
    def findTheDifference(self, s: str, t: str) -> str:
        ss=sorted(s)
        st=sorted(t)

        for i in range(len(ss)):
            if ss[i]!=st[i]:
                return st[i]

        return st[-1]



if __name__ == '__main__':
    init = FindTheDifference()
    print(init.findTheDifference("abcd", "abcde"))
    print(init.findTheDifference("abcd", "acbde"))
