from typing import List


class RemoveComments:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        buffer = []

        block_comment_on = False

        for line in source:
            llen = len(line)
            i = 0

            while i < llen:
                if line[i] == '/' and i < llen - 1 and line[i + 1] == '/' and not block_comment_on:
                    i = llen  # Ignore rest of sentence
                elif line[i] == '/' and i < llen - 1 and line[i + 1] == '*' and not block_comment_on:
                    block_comment_on = True
                    i += 2
                elif line[i] == '*' and i < llen - 1 and line[i + 1] == '/' and block_comment_on:
                    block_comment_on = False
                    i += 2
                elif block_comment_on:
                    i += 1
                elif not block_comment_on:
                    buffer.append(line[i])
                    i += 1
            if buffer and not block_comment_on:
                result.append(''.join(buffer))
                buffer.clear()
        return result

if __name__ == '__main__':
    init = RemoveComments()
    # source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
    #           "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    #
    # print(init.removeComments(source))
    # assert init.removeComments(source) == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]

    source=["a/*comment", "line", "more_comment*/b"]
    print(init.removeComments(source))
    assert init.removeComments(source) == ["ab"]


