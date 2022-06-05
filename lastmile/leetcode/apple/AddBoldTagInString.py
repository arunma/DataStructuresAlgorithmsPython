from typing import List


class AddBoldTagInString:
    # def addBoldTag(self, s: str, words: List[str]) -> str:
    #     if not words:
    #         return s
    #
    #     index=[]
    #
    #     for word in words:
    #         start = s.find(word)
    #         while start!=-1:
    #             end=start+len(word)
    #             index.append((start,end))
    #             start=s.find(word, end)
    #
    #     merged=[]
    #     if len(index)==1:
    #         merged=index
    #     elif len(index)==0:
    #         return s
    #     else:
    #         index.sort()
    #         mstart, mend=index[0]
    #         for start, end in index[1:]:
    #             if start<=mend:
    #                 mstart=min(start, mstart)
    #                 mend=max(end, mend)
    #             elif start>mend:
    #                 merged.append((mstart, mend))
    #                 mstart=start
    #                 mend=end
    #         merged.append((mstart, mend))
    #
    #     start=0
    #     end=len(s)
    #     result=''
    #     for mstart, mend in merged:
    #         result+=s[start:mstart]
    #         result+="<b>"
    #         result+=s[mstart:mend]
    #         result+="</b>"
    #         start=mend
    #     result+=s[merged[-1][1]:end]
    #     return result


    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s

        status=[False]*len(s)

        for word in words:
            start = s.find(word)
            while start!=-1:
                end=start+len(word)
                for i in range(start, end):
                    status[i]=True
                start=s.find(word, start+1)

        result=''

        i=0
        while i<len(s):
            if status[i]:
                result += "<b>"
                while i<len(s) and status[i]:
                    result += s[i]
                    i+=1
                result += "</b>"
            else:
                result+=s[i]
                i+=1

        return result



if __name__ == '__main__':
    init = AddBoldTagInString()
    print(init.addBoldTag(s = "abcxyz123", words = ["abc","123"]))
    print(init.addBoldTag(s = "aaabbcc", words = ["aaa","aab","bc"]))
    print(init.addBoldTag(s = "aaabbcc", words = ["d"]))
    print(init.addBoldTag(s = "aaabbcc", words = ["a", "b", "c"])) #"<b>a</b>aa<b>b</b>b<b>c</b>c"
