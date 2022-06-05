from typing import List


class PalindromePairs:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        store={word: i for i, word in enumerate(words)}
        result=[]
        for i, word in enumerate(words):
            N=len(word)
            for j in range(N+1):
                prefix=word[:j] #include empty space
                suffix=word[j:]
                if self.is_palin(prefix):
                    rev=suffix[::-1]
                    if rev!=word and rev in store:
                        result.append([store[rev], i])

                if j!=N and self.is_palin(suffix):
                    rev=prefix[::-1]
                    if rev!=word and rev in store:
                        result.append([store[rev], i])
        return result

    def is_palin(self, word):
        if word==word[::-1]:
            return True

if __name__ == '__main__':
    init = PalindromePairs()
    #print(init.palindromePairs(words = ["abcd","dcba","lls","s","sssll"]))
    print(init.palindromePairs(words = ["bat","tab","cat"]))
