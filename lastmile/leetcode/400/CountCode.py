class CountCode:
    def count_code(self, str):
        codes = set(["co"+c+"e" for c in str.lower()])
        count=0
        for i in range(4, len(str)+1):
            if str[i-4:i] in codes:
               count+=1

        return count



if __name__ == '__main__':
    init = CountCode()
    print(init.count_code('cozexxcope'))
    print(init.count_code('aaacodebbb'))
    print(init.count_code('codexxcode'))
