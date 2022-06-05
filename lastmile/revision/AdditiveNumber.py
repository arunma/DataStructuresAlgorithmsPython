class AdditiveNumber:
    def isAdditiveNumber(self, num: str) -> bool:
        N=len(num)
        if N<3:
            return False

        for i in range(1,N):
            for j in range(i+1, N):
                first = num[:i]
                second=num[i:j]
                if (first != '0' and first.startswith('0')) or (second!= '0' and second.startswith('0')):
                    continue
                rest = num[j:]
                while rest:
                    fstotal=int(first)+int(second)
                    if not rest.startswith(str(fstotal)):
                        break
                    else:
                        first=second
                        offset=len(str(fstotal))
                        second=rest[0:offset]
                        rest=rest[offset:]
                if not rest:
                    return True
        return False
    #
    # def isAdditiveNumber(self, num: str) -> bool:
    #     self.result=False
    #     self.recurse(num, None, None, 0, len(num))
    #     return self.result
    #
    # def recurse(self, num, first, second, succ_index, N):
    #     if (not num and succ_index==(N-1)) or self.result:
    #         self.result=True
    #         return
    #
    #     for i in range(len(num)):
    #         for j in range(i+1, N):
    #             if first==None and second==None:
    #                 first=num[:i]
    #                 second=num [i:j]
    #             else:
    #                 third=num[j:]
    #                 ntotal=int(first)+int(second)
    #                 if (first != '0' and first.startswith('0')) or (second != '0' and second.startswith('0')) or not third.startswith(str(ntotal)):
    #                     continue
    #                 else:
    #                     offset=len(str(ntotal))
    #                     third=third[offset:]
    #                     succ_index=j+offset
    #                     self.recurse(num, second, third, succ_index, N)





if __name__ == '__main__':
    init = AdditiveNumber()
    # print(init.isAdditiveNumber("112358")) #True
    # print(init.isAdditiveNumber("112359")) #False
    # print(init.isAdditiveNumber("199100199")) #True
    print(init.isAdditiveNumber("111122335588143")) #True

