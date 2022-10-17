class Cksum:
    def generate_cksum(self, s):
        cksum = 0
        N=len(s)
        byt=bytearray(s, 'utf-8')

        for i,b in enumerate(byt):
            print(s[i], b)
            cksum += b
        return cksum %256






if __name__ == "__main__":
    init = Cksum()
    print(init.generate_cksum("8=FIX.4.2\0019=49\00135=5\00134=1\00149=ARCA\00152=20150916-04:14:05.306\00156=TW\001")) #157
    #print(init.generate_cksum("8=FIX.4.2|9=49|35=5|34=1|49=ARCA|52=20150916-04:14:05.306|56=TW|"))
    #init.generate_cksum("8=FIX.4.2|9=49|35=5|34=1|49=ARCA|52=20150916-04:14:05.306|56=TW|10=157|")
