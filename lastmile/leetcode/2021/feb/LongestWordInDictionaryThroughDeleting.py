from typing import List


class LongestWordInDictionaryThroughDeleting:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda w: -len(w))
        for word in d:
            wi=0
            matches=0
            for c in s:
                if word[wi]==c:
                    matches+=1
                    wi+=1
                if matches==len(word):
                    return word
        return ""



if __name__ == '__main__':
    init = LongestWordInDictionaryThroughDeleting()
    print(init.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))
    print(init.findLongestWord(s = "abpcplea", d = ["a","b","c"]))