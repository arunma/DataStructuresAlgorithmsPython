class OneEditDistance:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        S = len(s)
        T = len(t)

        if S > T:
            return self.isOneEditDistance(t, s)

        if abs(S - T) > 1:
            return False

        for i in range(S):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]
        return True


if __name__ == '__main__':
    init = OneEditDistance()
    print(init.isOneEditDistance("a", ""))  # True
    print(init.isOneEditDistance("ab", "acb"))  # True
    print(init.isOneEditDistance("abcd", "abrd"))  # True
    print(init.isOneEditDistance("abcd", "abd"))  # True
    print(init.isOneEditDistance("acb", "ab"))  # True
    print(init.isOneEditDistance("acb", "arb"))  # True
    print(init.isOneEditDistance("acb", "abcdd"))  # False
    print(init.isOneEditDistance("cab", "ad"))  # False
