from collections import defaultdict, Counter


class MinimumStepsForAnagram:
    def minSteps(self, s: str, t: str) -> int:
        sdict=Counter(s)
        tdict=Counter(t)

        keys=set(list(sdict.keys()) + list(tdict.keys()))

        steps=0
        for key in keys:
            if key in sdict and key in tdict:
               steps+=abs(sdict[key]-tdict[key])
            elif key in sdict:
                steps+=sdict[key]
            else:
                steps+=tdict[key]
        return steps





if __name__ == '__main__':
    init = MinimumStepsForAnagram()
    #print(init.minSteps(s = "leetcode", t = "coats")) #7
    #print(init.minSteps(s = "night", t = "thing")) #0
    print(init.minSteps(s = "cotxazilut", t = "nahrrmcchxwrieqqdwdpneitkxgnt")) #27
