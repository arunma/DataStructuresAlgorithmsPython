from typing import List


class RestoreIPAddress:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result=[]
        self.backTrack(s, [], 0)
        return self.result


    def backTrack(self, s, curr, count):
        if count>4:
            return

        if count==4 and not s:
            self.result.append('.'.join(curr))
            return

        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0<int(s[:i])<256):
                self.backTrack(s[i:], curr+[s[:i]], count+1)


if __name__ == '__main__':
    init = RestoreIPAddress()
    print(init.restoreIpAddresses(s = "101023"))
    print(init.restoreIpAddresses(s = "010010"))
    print(init.restoreIpAddresses(s = "1111"))
    print(init.restoreIpAddresses(s = "0000"))
