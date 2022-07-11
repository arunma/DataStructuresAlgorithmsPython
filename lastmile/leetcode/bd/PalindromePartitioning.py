from typing import List


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.bt(s, [])
        return self.result

    def bt(self, s, curr):
        if not s:
            self.result.append(curr.copy())
            return

        for i in range(1, len(s)+1):
            if self.ispalin(s[:i]):
                self.bt(s[i:], curr + [s[:i]])

    def ispalin(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    init = PalindromePartitioning()
    print(init.partition(s = "aab")) #[["a","a","b"],["aa","b"]]
