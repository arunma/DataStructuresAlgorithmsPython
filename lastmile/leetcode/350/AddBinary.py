class AddBinary:
    def addBinary(self, ast: str, bst: str) -> str:
        #return bin(int(a,2) +int(b,2))[2:]
        a=list(ast)
        b=list(bst)

        carry=0
        result=''
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())

            result+=str(carry%2)
            carry=carry//2

        return result[::-1]




if __name__ == '__main__':
    init = AddBinary()
    print(init.addBinary("11", "1"))
    print(init.addBinary("1010", "1011"))
