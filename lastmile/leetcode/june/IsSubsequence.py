from collections import Counter


class IsSubsequence:
    def isSubsequence(self, sub: str, tar: str) -> bool:
        sl = len(sub)
        tl = len(tar)
        if sl > tl: return False
        if sl == 0: return True
        si = ti = 0
        while ti < tl:
            if sub[si] == tar[ti]:
                si = si + 1
                if si == sl:
                    return True
            ti = ti + 1
        return False


if __name__ == '__main__':
    init = IsSubsequence()
    print(init.isSubsequence("abc", "ahbgdc"))  # true
    print(init.isSubsequence("axc", "ahbgdc"))  # false
