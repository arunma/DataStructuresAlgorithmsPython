class ReverseString:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

if __name__ == '__main__':
    init = ReverseString()
    print(init.reverseWords("the sky is blue"))
    print(init.reverseWords("  hello world!  "))
