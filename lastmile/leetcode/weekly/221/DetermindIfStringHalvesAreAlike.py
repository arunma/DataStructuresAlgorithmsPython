class DetermindIfStringHalvesAreAlike:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        N=len(s)
        a=s[:N//2]
        b=s[N//2:]

        counta=0
        for c in a:
            if c in 'aeiou':
                counta+=1

        countb=0
        for c in b:
            if c in 'aeiou':
                countb+=1

        return counta==countb




if __name__ == '__main__':
    init = DetermindIfStringHalvesAreAlike()
    print(init.halvesAreAlike("textbook"))
    print(init.halvesAreAlike("book"))
    print(init.halvesAreAlike("AbCdEfGh"))
