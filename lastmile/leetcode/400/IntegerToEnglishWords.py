class IntegerToEnglishWords:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        self.lessThan10 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.lessThan20 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                           "Eighteen", "Nineteen"]
        self.lessThan100 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        return self.helper(num)

    def helper(self, num):
        result = ""
        if num < 10:
            result = self.lessThan10[num]
        elif num < 20:
            result = self.lessThan20[num - 10]
        elif num < 100:
            result = self.lessThan100[num // 10] + " " + self.helper(num % 10)
        elif num < 1000:
            result = self.helper(num // 100) + " Hundred " + self.helper(num % 100)
        elif num < 1000_000:
            result = self.helper(num // 1000) + " Thousand " + self.helper(num % 1000)
        elif num < 1000_000_000:
            result = self.helper(num // 1000_000) + " Million " + self.helper(num % 1000_000)
        else:
            result = self.helper(num // 1000_000_000) + " Billion " + self.helper(num % 1000_000_000)

        return result.strip()

    # def numberToWords1(self, num: int) -> str:
    #     if num == 0:
    #         return "Zero"
    #
    #     self.less_than_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    #     self.less_than_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
    #                              "Eighteen", "Nineteen"]
    #     self.less_than_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
    #                               "Ninety"]
    #
    #     return self.helper1(num)
    #
    # def helper1(self, num):
    #     result = ''
    #     if num < 10:
    #         result = self.less_than_ten[num]
    #     elif num < 20:
    #         result = self.less_than_twenty[num - 10]
    #     elif num < 100:
    #         result = self.less_than_hundred[num // 10] + " " + self.helper1(num % 10)
    #     elif num < 1000:
    #         result = self.helper1(num // 100) + " Hundred " + self.helper1(num % 100)
    #     elif num < 100000:
    #         result = self.helper1(num // 1000) + " Thousand " + self.helper1(num % 1000)
    #     elif num < 100000000:
    #         result = self.helper1(num // 1000000) + " Million " + self.helper1(num % 1000000)
    #     else:
    #         result = self.helper1(num // 1000000000) + " Billion " + self.helper1(num % 1000000000)
    #
    #     return result.strip()


if __name__ == '__main__':
    init = IntegerToEnglishWords()
    print(init.numberToWords(num=12345))
    print(init.numberToWords(num=1234567))
    print(init.numberToWords(num=1234567891))
