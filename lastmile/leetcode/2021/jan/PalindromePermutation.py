from collections import defaultdict


class PalindromePermutation:
    def canPermutePalindrome(self, s: str) -> bool:
        cmap=defaultdict(int)

        for c in s:
            cmap[c]+=1

        oddPresent=False
        for k,v in cmap.items():
            if v&1==1:
                if not oddPresent:
                    oddPresent=True
                else:
                    return False
        return True



if __name__ == '__main__':
    init = PalindromePermutation()
    print(init.canPermutePalindrome("aab")) #True
    print(init.canPermutePalindrome("carerac")) #True
    print(init.canPermutePalindrome("code")) #False
