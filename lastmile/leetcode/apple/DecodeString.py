
class DecodeString:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                word=''
                while stack[-1]!='[':
                    word=stack.pop()+word

                stack.pop()

                num=''
                while stack and stack[-1].isdigit():
                    num=stack.pop() + num

                stack.append(int(num)*word)

        return ''.join(stack)




if __name__ == '__main__':
    init = DecodeString()
    print(init.decodeString("100[leetcode]")) #"aaabcbc"
    print(init.decodeString("3[a]2[bc]")) #"aaabcbc"
    print(init.decodeString("3[a2[c]]")) #"accaccacc"


