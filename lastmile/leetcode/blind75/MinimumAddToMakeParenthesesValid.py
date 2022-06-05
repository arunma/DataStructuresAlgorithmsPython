class MinimumAddToMakeParenthesesValid:
    def minAddToMakeValid(self, s: str) -> int:
        left=right=0
        for c in s:
            if c=='(':
                right+=1
            elif c==')':
                if right>0:
                    right-=1
                else:
                    left+=1
        return left+right


if __name__ == '__main__':
    init = MinimumAddToMakeParenthesesValid()
    print(init.minAddToMakeValid(s="())"))  # 1
    print(init.minAddToMakeValid(s="((("))  # 3
