def knows(a: int, b: int) -> bool:
    return False
    # dt = {
    #     0: {0: True, 1: True, 2: False},
    #     1: {0: False, 1: True, 2: False},
    #     2: {0: True, 1: True, 2: True}
    # }


class FindTheCelebrity:
    def findCelebrity(self, n: int) -> int:
        celeb=0
        for o in range(1,n):
            if knows(celeb, o):
                celeb=o

        if self.is_celebrity(celeb, n):
            return celeb
        return -1

    def is_celebrity(self, c, n):
        for o in range(n):
            if o == c:
                continue
            elif knows(c, o) or not knows(o, c):
                return False
        return True


if __name__ == '__main__':
    init = FindTheCelebrity()
    print(init.findCelebrity(2))
