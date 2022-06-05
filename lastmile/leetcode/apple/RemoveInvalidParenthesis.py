from collections import deque
from typing import List




class RemoveInvalidParenthesis:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        self.bt(s, 0, 0, '', 0, result)
        return result

    def bt(self, s, left, right, curr, index, result):
        #print(curr)
        if left == right and index==len(s) and self.is_valid(curr):
            result.append(curr)
            return
        elif index >= len(s):
            return

        c= s[index]
        if c == '(':
            self.bt(s, left + 1, right, curr + '(', index+1, result)
            #self.bt(s, left, right, curr, index + 1, result)
        elif c == ')':
            if left > right:
                self.bt(s, left, right + 1, curr + ')', index+1, result)
                self.bt(s, left, right, curr, index + 1, result)
        else:
            self.bt(s, left, right, curr + c, index+1, result)

    def removeInvalidParentheses1(self, s: str) -> List[str]:
        seen=set()

        queue=deque([s])
        seen.add(s)

        while queue:
            level_size=len(queue)
            level_result=[]
            for _ in range(level_size):
                curr=queue.popleft()
                if self.is_valid(curr):
                    level_result.append(curr)
                else:
                    for i in range(len(curr)):
                        if curr[i] not in "()": continue
                        next=curr[:i]+curr[i+1:]
                        if next not in seen:
                            seen.add(next)
                            queue.append(next)

            if level_result:
                return level_result

        return [""]

    def is_valid(self, s):
        score=0
        for c in s:
            if c=='(':
                score+=1
            if c==')':
                score-=1
            if score<0:
                return False
        return score==0


if __name__ == '__main__':
    init = RemoveInvalidParenthesis()
    print(init.removeInvalidParentheses("()())()"))  # ["(())()","()()()"]
    print(init.removeInvalidParentheses("(a)())()"))  # ["(a())()","(a)()()"]
    print(init.removeInvalidParentheses(s=")("))  # [""]
    print(init.removeInvalidParentheses("x("))  # ["x"]
    print(init.removeInvalidParentheses(")(f"))  # ["f"]

