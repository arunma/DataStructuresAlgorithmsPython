from typing import List


class StringCompression:
    def compress(self, chars: List[str]) -> int:
        index=0
        N=len(chars)

        result=[]
        while index<N:
            char=chars[index]
            result.append(char)
            count=0
            while index<N and chars[index]==char:
                count+=1
                index+=1
            result.append(count)

        return result





if __name__ == '__main__':
    init = StringCompression()
    print(init.compress(["a","a","b","b","c","c","c"]))
