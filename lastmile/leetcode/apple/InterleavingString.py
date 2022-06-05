class InterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.result = False
        self.dfs(s1, s2, s3, 0, 0, 0, set())
        return self.result

    def dfs(self, s1, s2, s3, s1i, s2i, s3i, cache):
        if s1i*s3i+s2i in cache:
            return
        if s1i == len(s1) and s2i == len(s2) and s3i == len(s3):
            self.result = True
            return
        if s3i == len(s3) and (s1i<len(s1) or s2i<len(s2)):
            self.result=False
            return

        cache.add(s1i*s3i+s2i)
        if s1i < len(s1) and s3[s3i] == s1[s1i]:
            self.dfs(s1, s2, s3, s1i + 1, s2i, s3i + 1, cache)
        if s2i < len(s2) and s3[s3i] == s2[s2i]:
            self.dfs(s1, s2, s3, s1i, s2i + 1, s3i + 1, cache)


if __name__ == '__main__':
    init = InterleavingString()
    #print(init.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    #print(init.isInterleave("a", "b", "a"))
    print(init.isInterleave("def", "", "de"))
