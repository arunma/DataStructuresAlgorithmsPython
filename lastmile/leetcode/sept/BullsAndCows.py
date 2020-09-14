from collections import defaultdict, Counter


class BullsAndCows:
    def getHint(self, secret: str, guess: str) -> str:

        scounter = Counter(secret)
        gcounter = Counter(guess)

        bulls = 0

        for i, sval in enumerate(secret):
            if sval == guess[i]:
                bulls += 1

        intersect = sum((scounter & gcounter).values())
        cows = intersect-bulls

        return "{}A{}B".format(bulls, cows)


if __name__ == '__main__':
    init = BullsAndCows()
    print(init.getHint(secret="1807", guess="7810")) #1A3B
    print(init.getHint(secret="1123", guess="0111")) #1A1B
    print(init.getHint(secret="1122", guess="1222"))  # "3A0B"
