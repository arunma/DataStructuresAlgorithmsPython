from collections import Counter


class DetermineIfTwoStringsAreClose:
    def closeStrings(self, word1: str, word2: str) -> bool:
        N=len(word1)
        M=len(word2)

        if N!=M:
            return False

        count1=Counter(word1)
        count2=Counter(word2)

        freq1=set(count1.values())
        freq2=set(count2.values())

        return freq1==freq2 and count1.keys()==count2.keys()




if __name__ == '__main__':
    init = DetermineIfTwoStringsAreClose()
    print(init.closeStrings(word1 = "abc", word2 = "bca")) #True
    print(init.closeStrings(word1 = "cabbba", word2 = "abbccc")) #True
    print(init.closeStrings(word1 = "a", word2 = "aa")) #False
    print(init.closeStrings(word1 = "cabbba", word2 = "aabbss")) #False
