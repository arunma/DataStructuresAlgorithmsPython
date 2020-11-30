class MaximumRepeatingSubstring:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        for i in range(1,100):
            w=word*i
            if w in sequence:
                k+=1
            else:
                break
        return k

if __name__ == '__main__':
    init = MaximumRepeatingSubstring()
    print(init.maxRepeating("ababc", "ba"))
    print(init.maxRepeating("ababc", "ab"))
    print(init.maxRepeating("baba", "b"))
    print(init.maxRepeating("aaa", "a"))
