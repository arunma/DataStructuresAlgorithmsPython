from collections import defaultdict
from typing import List

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for st in strs:
            group[tuple((sorted(st)))].append(st)
        return list(group.values())


if __name__ == '__main__':
    init = GroupAnagrams()
    print(init.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

