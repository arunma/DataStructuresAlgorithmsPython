from typing import List


class PalindromePermutationII:
    def generatePalindromes(self, s: str) -> List[str]:
        s=sorted(s)
        self.result=[]
        self.bt(s, '', len(s))
        return self.result

    def bt(self, s, curr, N):
        if not s and len(curr)==N and self.ispalin(curr):
            self.result.append(curr)
            return

        for i in range(len(s)):
            if i>0 and s[i-1]==s[i]:
                continue
            else:
                self.bt(s[:i]+s[i+1:], curr+s[i], N)

    def ispalin(self, s):
        return s==s[::-1]


if __name__ == '__main__':
    init = PalindromePermutationII()
    print(init.generatePalindromes(s = "aabb")) #Output: ["abba","baab"]
