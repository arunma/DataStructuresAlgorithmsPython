from typing import List


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        N = len(digits)

        result = []

        for i in reversed(range(N)):
            digit = digits[i]
            total = digit + carry
            carry, value = divmod(total, 10)

            result.append(value)
            # if carry == 0: # Optimization
            #     result.reverse()
            #     return digits[:i] + result

        if carry!=0:
            result.append(carry)
        result.reverse()
        return result

if __name__ == '__main__':
    init = PlusOne()
    print(init.plusOne([1,2,3]))
    print(init.plusOne([9,9,9]))
