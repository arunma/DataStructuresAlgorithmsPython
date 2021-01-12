class CountOfMatchesInTournament:
    def numberOfMatches(self, n: int) -> int:
        count=0
        while n>1:
            count+=n//2
            if n&1:
                n=(n//2)+1
            else:
                n=n//2
        return count


if __name__ == '__main__':
    init = CountOfMatchesInTournament()
    print(init.numberOfMatches(7))
    print(init.numberOfMatches(14))
