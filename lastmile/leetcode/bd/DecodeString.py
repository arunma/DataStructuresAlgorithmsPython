class DecodeString:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c!=']':
                stack.append(c)
            else:
                ele=''
                while stack and stack[-1]!='[':
                    ele=stack.pop()+ele
                stack.pop() #pop '['

                count = ''
                while stack and stack[-1].isdigit():
                    count=stack.pop()+count
                stack.append(int(count)*ele)

        return ''.join(stack)


if __name__ == '__main__':
    init = DecodeString()
    print(init.decodeString("100[leetcode]"))  # "aaabcbc"
    #print(init.decodeString("3[a]2[bc]"))  # "aaabcbc"
    #print(init.decodeString("3[a2[c]]"))  # "accaccacc"
