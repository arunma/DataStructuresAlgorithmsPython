from typing import List


class MaxParenthesisDepthAfterSplit:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result=[]
        depth=0

        for c in seq:
            if c=='(':
                depth+=1
            result.append(depth%2)
            if c==')':
                depth-=1
        return result



if __name__ == '__main__':
    init = MaxParenthesisDepthAfterSplit()
    print(init.maxDepthAfterSplit("(()())"))
