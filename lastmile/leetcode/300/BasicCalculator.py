class BasicCalculator:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-/*" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = c
                num=0
        return sum(stack)


if __name__ == '__main__':
    init = BasicCalculator()
    #print(init.calculate("3+2*2")) #7
    #print(init.calculate("3/2")) #1
    #print(init.calculate(" 3+5 / 2 ")) #5
    print(init.calculate("14-3/2")) #13
