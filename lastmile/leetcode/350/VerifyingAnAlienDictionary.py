from typing import List


class VerifyingAnAlienDictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord={c:i for i, c in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):
            if len(word1)>len(word2) and word1[:len(word2)]==word2:
                return False
            for c1, c2 in zip(word1, word2):
                if ord[c1]<ord[c2]:
                    break #Different characters. Check only for the first difference
                if ord[c1]>ord[c2]:
                    return False
        return True




if __name__ == '__main__':
    init = VerifyingAnAlienDictionary()
    print(init.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")) #True
    print(init.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")) #False
