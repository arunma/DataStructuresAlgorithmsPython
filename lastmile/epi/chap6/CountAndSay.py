class CountAndSay:
    def countAndSay(self, n: int) -> str:
        s='1'
        for i in range(n-1):
            count=1
            temp=[]
            for i in range(1, len(s)):
                if s[i-1]==s[i]:
                    count+=1
                else:
                    temp.append(str(count))
                    temp.append(s[i-1])
                    count=1
            temp.append(str(count))
            temp.append(s[-1])
            s=''.join(temp)
        return s



if __name__ == '__main__':
    init = CountAndSay()
    print(init.countAndSay(4)) #1211
