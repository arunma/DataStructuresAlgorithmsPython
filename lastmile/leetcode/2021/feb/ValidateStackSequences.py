from typing import List


class ValidateStackSequences:
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     popi = 0
    #     pushi = 0
    #
    #     stack = []
    #     while pushi < len(pushed):
    #         stack.append(pushed[pushi])
    #         pushi += 1
    #         while stack and stack[-1] == popped[popi]:
    #             stack.pop()
    #             popi += 1
    #     return len(stack) == 0

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popi = 0
        stack = []
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[popi]:
                stack.pop()
                popi += 1
        return not stack

if __name__ == '__main__':
    init = ValidateStackSequences()
    print(init.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])) #True
    print(init.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])) #False
