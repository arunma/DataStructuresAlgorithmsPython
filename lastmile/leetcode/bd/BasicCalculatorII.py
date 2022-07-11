class BasicCalculatorII:
    def calculate(self, s: str) -> int:
        op='+'
        num=0
        stack=[]

        for i,c in enumerate(s):
            if c.isdigit():
                num=num*10+int(c)
            elif c in "+-*/":
                self.update_stack(op, stack, num)
                num=0
                op=c
        self.update_stack(op, stack, num)
        return sum(stack)

    def update_stack(self, op, stack, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            prev = stack.pop()
            stack.append(prev * num)
        elif op == '/':
            prev = stack.pop()
            stack.append(int(prev / num))




if __name__ == '__main__':
    init = BasicCalculatorII()
    print(init.calculate("3+2*2")) #7
    print(init.calculate("3/2")) #1
    print(init.calculate("3+5/2")) #5
