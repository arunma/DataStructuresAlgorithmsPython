from collections import defaultdict
from typing import List


class GroupShiftedStrings:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for s in strings:
            key=[]
            for i in range(1, len(s)):
                circDiff= 26 + ord(s[i]) - ord(s[i - 1])
                key.append(circDiff%26)

            map[tuple(key)].append(s)
        return list(map.values())






if __name__ == '__main__':
    init = GroupShiftedStrings()
    print(init.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
