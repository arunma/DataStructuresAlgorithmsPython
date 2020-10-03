class RearrangeSpacesBetweenWords:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for i, c in enumerate(text):
            if c == ' ':
                spaces += 1
        words = [word for word in text.split(" ") if word.strip() != '']
        if spaces == 0:
            return text

        if len(words)==1:
            return words[0].strip() +' '*spaces

        between, last = divmod(spaces, len(words) - 1)
        result = ""
        for word in words[:-1]:
            result += word
            result += " " * between

        if last:
            result += words[-1]
            result += " " * last
        else:
            result += words[-1]

        return result


if __name__ == '__main__':
    init = RearrangeSpacesBetweenWords()
    # print(init.reorderSpaces(text="  this   is  a sentence "), "'")
    # print(init.reorderSpaces(text=" practice   makes   perfect"))
    # print(init.reorderSpaces(text="a"))
    print(init.reorderSpaces(text=" hello"))
