class BasicCalculatorIII:
    def calculate(self, s: str) -> int:
        result, _ = self.calculate_inner(s)
        return result

    def calculate_inner(self, s):

        op = '+'
        num = 0
        stack = []

        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                self.update_stack(stack, num, op)
                num = 0
                op = c
            elif c == '(':
                num, j = self.calculate_inner(s[i + 1:])
                i += j
            elif c == ')':
                self.update_stack(stack, num, op)
                return sum(stack), i + 1
            i += 1
        self.update_stack(stack, num, op)
        return sum(stack), -1

    def update_stack(self, stack, num, op):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            prev = stack.pop()
            stack.append(prev * num)
        elif op == '/':
            prev = stack.pop()
            stack.append(int(prev/num))



if __name__ == '__main__':
    init = BasicCalculatorIII()
    #print(init.calculate("1 + 1")) #2
    #print(init.calculate(" 2-1 + 2 ")) #3
    #print(init.calculate("(1+(4+5+2)-3)+(6+8)")) #23
    print(init.calculate("5-3/2")) #4
