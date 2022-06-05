from collections import defaultdict
from typing import List

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap=defaultdict(list)
        for s in strs:
            wordmap[tuple(sorted(s))].append(s)

        return list(wordmap.values())


if __name__ == '__main__':
    init = GroupAnagrams()
    print(init.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    #[["bat"],["nat","tan"],["ate","eat","tea"]]
