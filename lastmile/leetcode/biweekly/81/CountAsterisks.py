class CountAsterisks:
    def countAsterisks(self, s: str) -> int:
        pipes=[]
        for i,c in enumerate(s):
            if c=='|':
                pipes.append(i)

        count = 0
        if not pipes:
            for c in s:
                if c == '*':
                    count += 1
            return count



        for c in s[0:pipes[0]]:
            if c == '*':
                count += 1

        for c in s[pipes[-1]:]:
            if c == '*':
                count += 1

        for i in range(1, len(pipes), 2):
            if i+1>=len(pipes):
                break
            string = s[pipes[i]:pipes[i+1]]
            for c in string:
                if c=='*':
                    count+=1
        return count







if __name__ == '__main__':
    init = CountAsterisks()
    print(init.countAsterisks("l|*e*et|c**o|*de|")) #2
    print(init.countAsterisks("yo|uar|e**|b|e***au|tifu|l")) #5
    print(init.countAsterisks("iamprogrammer")) #0
    print(init.countAsterisks("*||*|||||*|*|***||*||***|")) #3
    print(init.countAsterisks("*jsaxclgfcyjds")) #1
