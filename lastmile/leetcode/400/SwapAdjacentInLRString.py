class SwapAdjacentInLRString:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False

        slist = [(idx, ch) for idx, ch in enumerate(start) if ch == 'L' or ch == 'R']
        elist = [(idx, ch) for idx, ch in enumerate(end) if ch == 'L' or ch == 'R']

        #Important
        if len(slist) != len(elist):
            return False

        for (i, s), (j, e) in zip(slist, elist):
            if s != e:
                return False
            if s == 'L':
                if j > i:
                    return False
            elif s == 'R':
                if j < i:
                    return False
        return True


if __name__ == '__main__':
    init = SwapAdjacentInLRString()
    print(init.canTransform(start="RXXLRXRXL", end="XRLXXRRLX"))  # True
    print(init.canTransform("LXXLXRLXXL", "XLLXRXLXLX"))  # False
    # print(init.canTransform("X","L")) #False
    # print(init.canTransform("LLR","RRL")) #False
