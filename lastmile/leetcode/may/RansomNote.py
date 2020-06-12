class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map = {}
        for m in magazine:
            freq_map[m]=freq_map.get(m, 0)+1

        for r in ransomNote:
            if r in freq_map:
                freq_map[r] -= 1
                if freq_map[r] < 0:
                    return False
            else:
                return False

        return True


if __name__ == '__main__':
    init = RansomNote()
    print(init.canConstruct("a", "b"))  # false
    print(init.canConstruct("aa", "ab"))  # false
    print(init.canConstruct("aa", "aab"))  # true
