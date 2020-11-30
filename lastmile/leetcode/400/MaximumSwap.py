class MaximumSwap:
    # def maximumSwap(self, num: int) -> int:
    #     A = list(str(num))
    #     last = {int(x): i for i, x in enumerate(A)}
    #     for i, x in enumerate(A):
    #         for d in range(9, int(x), -1):
    #             if last.get(d, 0) > i:
    #                 A[i], A[last[d]] = A[last[d]], A[i]
    #                 return int("".join(A))
    #     return num

    def maximumSwap(self, num: int) -> int:
        A=list(str(num))
        last={int(x):i for i, x in enumerate(A)}

        for i, x in enumerate(A):
            for d in range(9, int(x), -1):
                if last.get(d, 0)>i:
                    A[i], A[last[d]]=A[last[d]], A[i]
                    return int(''.join(A))
        return num

    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        last = {int(x): i for i, x in enumerate(A)}

        for i, x in enumerate(A):
            for d in range(9, int(x), -1):
                if d in last and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int(''.join(A))

        return num




if __name__ == '__main__':
    init = MaximumSwap()
    print(init.maximumSwap(78361))
    print(init.maximumSwap(2736))
    print(init.maximumSwap(6798))
