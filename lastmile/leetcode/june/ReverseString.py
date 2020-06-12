from typing import List


class ReverseString:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while (i <= j):
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1


if __name__ == '__main__':
    init = ReverseString()
    print(init.reverseString(["h", "e", "l", "l", "o"]))
    print(init.reverseString(["H", "a", "n", "n", "a", "h"]))
