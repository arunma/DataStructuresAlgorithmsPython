import collections
from collections import Counter


class NumberOfAtoms:
    def countOfAtoms(self, formula: str) -> str:
        counter = Counter()
        stack = []

        ele = ''
        weight = 1
        count = 0

        for c in formula[::-1]:
            if c.isdigit():
                count = count*10 + int(c)
            elif c == ')':
                stack.append(count)
                weight = weight * count
                count = 0
            elif c=='(':
                lastweight=stack.pop()
                weight=weight//(lastweight or 1)
                count = 0
            elif c.islower():
                ele = c + ele
            elif c.isupper():
                ele = c + ele
                counter[ele]+=weight* (count or 1)
                count = 0
                ele=''

        result=[f"{k}{v if v>1 else ''}" for k,v in sorted(counter.items())]
        return ''.join(result)


    #
    # def countOfAtoms(self, formula):
    #     dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], "", 0, 0
    #     for c in formula[::-1]:
    #         if c.isdigit():
    #             cnt += int(c) * (10 ** i)
    #             i += 1
    #         elif c == ")":
    #             stack.append(cnt)
    #             coeff *= cnt
    #             i = cnt = 0
    #         elif c == "(":
    #             coeff //= stack.pop()
    #             i = cnt = 0
    #         elif c.isupper():
    #             elem += c
    #             dic[elem[::-1]] += (cnt or 1) * coeff
    #             elem = ""
    #             i = cnt = 0
    #         elif c.islower():
    #             elem += c
    #     return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))


if __name__ == '__main__':
    init = NumberOfAtoms()
    print(init.countOfAtoms("H2O"))  # "H2O"
    print(init.countOfAtoms("Mg(OH)2"))  #"H2MgO2"
    print(init.countOfAtoms("K4(ON(SO3)2)2"))  # "K4N2O14S4"
    print(init.countOfAtoms("(H)"))  #H
    print(init.countOfAtoms("Mg(H2O)N"))  #
