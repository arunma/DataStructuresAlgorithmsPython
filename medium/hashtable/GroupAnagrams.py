from collections import defaultdict
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gwords = defaultdict(list)

        for each in strs:
            gwords[tuple(sorted(each))].append(each)

        return gwords.values()


if __name__ == "__main__":
    init = GroupAnagrams()
    x= init.groupAnagrams( ["eat","tea","tan","ate","nat","bat"])
    print(x)
