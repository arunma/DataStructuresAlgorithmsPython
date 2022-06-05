class EncordAndDecodeStrings:
    def encode(self, strs: [str]) -> str:
        return ''.join(f'{len(s)}:{s}' for s in strs)

    def decode(self, s: str) -> [str]:
        strs=[]
        i=0
        while i<len(s):
            coli=s.find(":", i)
            size=int(s[i:coli])
            cand=s[coli+1:coli+size+1]
            strs.append(cand)
            i=coli+size+1
        return strs



if __name__ == '__main__':
    init = EncordAndDecodeStrings()
    strs=["Hello", "Worl"]
    out=init.encode(strs)
    print(out)
    print(init.decode(out))
