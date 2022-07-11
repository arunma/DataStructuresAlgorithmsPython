from string import ascii_lowercase

class DecodeTheMessage:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(" ", "")
        #map = {a:k for a,k in zip(key, ascii_lowercase)}

        i=0
        mapp={}
        for k in key:
            if k==' ':
                continue
            elif k not in mapp:
                mapp[k.strip()]=ascii_lowercase[i]
                print(k, i, ascii_lowercase[i])
                i+=1


        result=[]
        for c in message:
            if c==' ':
                result.append(" ")
            else:
                result.append(mapp[c])

        return ''.join(result)

if __name__ == '__main__':
    init = DecodeTheMessage()
    print(init.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
