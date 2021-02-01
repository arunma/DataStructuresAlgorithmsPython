from collections import Counter


class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter=Counter(magazine)
        for r in ransomNote:
            if r not in counter:
                return False
            else:
                if counter[r]==0:
                    return False
                counter[r]-=1
        return True


if __name__ == '__main__':
    init = RansomNote()
    print(init.canConstruct("a", "b")) #false
    print(init.canConstruct("aa", "ab")) #false
    print(init.canConstruct("aa", "aab")) #True
