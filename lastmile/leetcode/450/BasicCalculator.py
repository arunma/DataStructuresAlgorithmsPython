class BasicCalculator:
    def calculate(self, s: str) -> int:
        sign = '+'
        curr = 0

        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(curr)
                elif sign == '-':
                    stack.append(-curr)
                elif sign == '*':
                    stack.append(stack.pop() * curr)
                elif sign == '/':
                    stack.append(stack.pop() // curr)
                sign = c
                curr = 0

        return sum(stack)


if __name__ == '__main__':
    init = BasicCalculator()
    print(init.calculate("14-3/2"))
