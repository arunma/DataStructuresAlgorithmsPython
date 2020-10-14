# class RemoveKthElementUntilLast:
# list: A, B, C, D, E
# k: 3
# round1: A, B, D, E
# C is deleted
# round2: B, D, E
# A is deleted
# round3: B, D
# E is deleted
# round4: D
# B is deleted
# return D
#
# A, B, C, D, E, F, G
# A, B, D, E, F, G
# A, B, D, E, G
# A， D， E， G
# ADE
# AD
# D
#
# AD = 2
# start = 3

# def getLast(chars, k):
#     if not chars:
#         return -1
#     if len(chars) == 1:
#         return chars[0]
#     start = 0
#     while len(chars) > 1:
#         start += k - 1
#         if start >= len(chars):
#             start = start % len(chars)
#         del chars[start]
#
#     return chars[0]

def getLast1(chars, k):
    if not chars:
        return -1

    N = len(chars)
    if N == 1:
        return chars[0]
    if N < k:
        return chars[k % N]
    # start = k-1
    k -= 1
    start = k
    while len(chars) > 1:
        # start += k - 1
        del chars[start]
        # if start >= len(chars):
        start = (start + k) % len(chars)
    return chars[0]


def getLast2(chars, k):
    if not chars:
        return -1

    N = len(chars)
    if N == 1:
        return chars[0]
    if N < k:
        return chars[k % N]
    k -= 1
    start = k
    while len(chars) > 1:
        del chars[start]
        start = (start + k) % len(chars)
    return chars[0]


def getLast(chars, k):
    if not chars:
        raise Exception("Empty array")

    N = len(chars)
    if N == 1:
        return chars[0]
    if N < k:
        return chars[k % N]
    k -= 1
    start = k
    while len(chars) > 1:
        del chars[start]
        start = (start + k) % len(chars)
    return chars[0]


def josephus(ls, skip):
    skip -= 1  # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        ls.pop(idx)
        # print(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    return ls[0]
    # print('survivor: ', ls[0])


if __name__ == '__main__':
    print(getLast(["A", "B", "C", "D", "E"], 3))
    print(getLast(["A", "B", "C", "D", "E", "F"], 3))
    print(getLast(["A", "B"], 3))
    print(getLast(["A"], 3))
    print(getLast([], 3))
    # print(josephus(["A", "B"], 3))
    # print(josephus(["A", "B", "C", "D", "E", "F"], 3))
    # print(josephus(["A", "B", "C", "D", "E"], 3))
    # print(josephus(["A"], 3))

"""
start=0, A, B, C, D, E
start=2, A, B, /C/, D, E
start=(4, A, B, D, E 


"""
