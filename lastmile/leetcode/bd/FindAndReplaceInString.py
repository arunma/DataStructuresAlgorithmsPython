from typing import List


class FindAndReplaceInString:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = ''
        lookup={i:(s,t) for (i,s,t) in zip(indices, sources, targets)}

        i=0
        while i<len(s):
            if i in lookup and s[i:].startswith(lookup[i][0]):
                result+=lookup[i][1]
                i+=len(lookup[i][0])
            else:
                result+=s[i]
                i+=1
        return result




if __name__ == '__main__':
    init = FindAndReplaceInString()
    #print(init.findReplaceString(s="abcd", indices=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))  # "eeebffff"
    #print(init.findReplaceString(s="abcd", indices=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))  # "eeecd"
    print(init.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"])) #"vbfrssozp"
    print(init.findReplaceString("abcd",[0, 2],["ab","ec"],["eee","ffff"])) #"eeecd"
    print(init.findReplaceString("jjievdtjfb",[4,6,1],["md","tjgb","jf"],["foe","oov","e"])) #"jjievdtjfb"

