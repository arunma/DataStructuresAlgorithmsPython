class RemoveDuplicates:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        lasti = {}
        visited=set()

        for i, c in enumerate(s):
            lasti[c] = i

        for i,c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and lasti[stack[-1]]>i:
                    ctemp = stack.pop()
                    visited.remove(ctemp)

                stack.append(c)
                visited.add(c)

        return ''.join(stack)


if __name__ == '__main__':
    init = RemoveDuplicates()
    #print(init.removeDuplicateLetters("bcabc")) #abc
    print(init.removeDuplicateLetters("cbacdcbc")) #"acdb"
