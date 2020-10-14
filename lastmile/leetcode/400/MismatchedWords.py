class MismatchedWords:
    def findMismatched(self, s1, s2):
        set1=set(s1.split())
        set2=set(s2.split())

        result=set1^set2
        return result


if __name__ == '__main__':
    init = MismatchedWords()
    print(init.findMismatched("Firstly this is the first string", "Next is the second string")
)
