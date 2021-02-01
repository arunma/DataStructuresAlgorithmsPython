from collections import Counter


class PalindromePermutation:
    def canPermutePalindrome(self, s: str) -> bool:
        counter=Counter(s)
        oddFound=False
        for ch,cnt in counter.items():
            if cnt%2==1:
                if oddFound==False:
                    oddFound=True
                else:
                    return False
        return True

if __name__ == '__main__':
    init = PalindromePermutation()
    print(init.canPermutePalindrome('code'))
    print(init.canPermutePalindrome('aab'))
