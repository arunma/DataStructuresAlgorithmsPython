class MinimumRemoveToMakeValidParantheses:
    def minRemoveToMakeValid(self, s: str) -> str:
        slist = list(s)
        stack = []

        for i, c in enumerate(slist):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    slist[i] = ''

        while stack:
            slist[stack.pop()] = ''

        return ''.join(slist)

if __name__ == '__main__':
    init = MinimumRemoveToMakeValidParantheses()
    print(init.minRemoveToMakeValid("lee(t(c)o)de)")) #lee(t(c)o)de
