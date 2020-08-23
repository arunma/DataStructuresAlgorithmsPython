class ThousandSeparator:
    def thousandSeparator(self, n: int) -> str:
        res=[]
        point=0
        for s in reversed(str(n)):
            point+=1
            res.append(s)
            if point==3:
                point=0
                res.append(".")
        if res[-1]=='.':
            res.pop()
        return "".join(reversed(res))





if __name__ == '__main__':
    init = ThousandSeparator()
    print(init.thousandSeparator(987))
    print(init.thousandSeparator(1234))
    print(init.thousandSeparator(123456789))
    print(init.thousandSeparator(0))
    print(init.thousandSeparator(51040))
