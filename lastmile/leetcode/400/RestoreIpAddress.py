from typing import List


class RestoreIpAddress:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        curr = []
        self.backtrack(result, s, curr, 0)
        return result

    def backtrack(self, result, s, curr, index):
        if len(curr) == 4 and index == len(s):
            result.append('.'.join(curr))
        if len(curr) > 4:
            return
        for i in range(index, min(index + 4, len(s))):
            cand = s[index:i + 1]
            if cand == '0' or (cand[0] != '0' and 0 < int(cand) < 256):
                self.backtrack(result, s, curr + [cand], i + 1)


if __name__ == '__main__':
    init = RestoreIpAddress()
    print(init.restoreIpAddresses("25525511135"))
    # print(init.restoreIpAddresses("101023"))
