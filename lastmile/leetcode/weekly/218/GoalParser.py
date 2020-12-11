class GoalParser:
    def interpret(self, command: str) -> str:
        if not command:
            return ''
        result=[]

        while command:
            if command.startswith("G"):
                result.append("G")
                command=command[1:]
            elif command.startswith("()"):
                result.append("o")
                command = command[2:]
            elif command.startswith("(al)"):
                result.append("al")
                command = command[4:]
        return ''.join(result)

if __name__ == '__main__':
    init = GoalParser()
    print(init.interpret("G()(al)")) # "Goal"
    print(init.interpret("G()()()()(al)")) # "Gooooal"
    print(init.interpret("(al)G(al)()()G")) # "alGalooG"
