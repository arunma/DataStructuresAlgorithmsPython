from typing import List


class SequentialDigits:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits="123456789"

        startDigits=len(str(low))
        endDigits=len(str(high))

        result=[]
        for step in range(startDigits, endDigits+1):
            for i in range(len(digits)-step+1):
                curr = int(digits[i:i + step])
                if low<=curr<=high:
                    result.append(curr)
        return result


if __name__ == '__main__':
    init = SequentialDigits()
    print(init.sequentialDigits(low = 100, high = 300))
    print(init.sequentialDigits(low = 1000, high = 13000))
    print(init.sequentialDigits(low = 234, high = 2314))