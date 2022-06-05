from collections import deque


class BasicCalculator:
    def calculate(self, s: str) -> int:
        sign="+"
        curr=0
        stack=deque()
        i=0

        def update(curr, sign):
            if sign=='+':
                stack.append(curr)
            elif sign=='-':
                stack.append(-curr)
            elif sign=='*':
                prev=stack.pop()
                stack.append(curr*prev)
            elif sign=='/':
                prev = stack.pop()
                stack.append(prev//curr)


        while i<len(s):
            if s[i].isdigit():
                curr=curr*10+int(s[i])
            elif s[i] in "+-*/":
                update(curr, sign)
                curr=0
                sign=s[i]
            elif s[i]=='(':
                curr, j = self.calculate(s[i+1:])
                i+=j
            elif s[i]==')':
                update(curr, sign)
                return sum(stack), i+1
            i+=1

        update(curr, sign)
        return sum(stack)








if __name__ == '__main__':
    init = BasicCalculator()
    #print(init.calculate("1 + 1")) #2
    print(init.calculate(" 2-1 + 2 ")) #3
    print(init.calculate("(1+(4+5+2)-3)+(6+8)")) #23
