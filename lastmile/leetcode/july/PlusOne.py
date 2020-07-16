from typing import List


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        _sum = 1 + digits[-1]
        carry = _sum // 10
        digits[-1] = _sum % 10

        n = N - 2
        while carry != 0 and n>=0:
            _sum = digits[n] + carry
            digits[n] = _sum % 10
            carry = _sum // 10
            n = n - 1

        if carry != 0:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    init = PlusOne()
    print(init.plusOne([1, 2, 3]))  # 124
    print(init.plusOne([4, 3, 2, 1]))  # 4322
    print(init.plusOne([9,9,9]))  # 1000
