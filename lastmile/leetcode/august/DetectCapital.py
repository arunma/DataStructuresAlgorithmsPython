import re


class DetectCapital:
    def detectCapitalUse(self, word: str) -> bool:
        return bool(re.fullmatch(r"[A-Z]*|.[a-z]*", word))

if __name__ == '__main__':
    init = DetectCapital()
    print(init.detectCapitalUse("USA")) #True
    print(init.detectCapitalUse("FlaG")) #False
    print(init.detectCapitalUse("leetcode")) #True
