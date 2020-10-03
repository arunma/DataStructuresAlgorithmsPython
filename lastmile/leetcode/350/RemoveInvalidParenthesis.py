from typing import List


class RemoveInvalidParenthesis:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = [s]

        seen = set()
        found = False
        result = []
        while queue:
            curr = queue.pop(0)
            if curr not in seen:
                seen.add(curr)

                if self.isValid(curr):
                    found = True
                    result.append(curr)
                if found:
                    continue
                else:
                    for i in range(len(curr)):
                        if curr[i] not in "()":
                            continue
                        queue.append(curr[:i] + curr[i + 1:])

        return result

    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0



# def removeInvalidParentheses(self, s: str) -> List[str]:
    #     queue = []
    #     queue.append(s)
    #     seen = set()
    #
    #     result = []
    #     found=False
    #
    #     while (queue):
    #         curr = queue.pop(0)
    #         if curr not in seen:
    #             seen.add(curr)
    #             if self.isValid(curr):
    #                 result.append(curr)
    #                 found=True
    #             if found:
    #                 continue
    #             else:
    #                 for i in range(len(curr)):
    #                     if curr[i] != '(' and curr[i] != ')':
    #                         continue
    #                     nxt = curr[:i] + curr[i + 1:]
    #                     if nxt not in seen:
    #                         queue.append(nxt)
    #     return result
    #
    # def isValid(self, curr):
    #     count = 0
    #     for i in range(len(curr)):
    #         if curr[i] == '(':
    #             count += 1
    #         elif curr[i] == ')':
    #             count -= 1
    #             if count<0:
    #                 return False
    #     return count == 0


if __name__ == '__main__':
    init = RemoveInvalidParenthesis()
    print(init.removeInvalidParentheses("()())()"))  # ["()()()", "(())()"]
