class NextPower2:
    def next_pow2(self, v):
        v-=1
        v |= v>>1
        v |= v>>2
        v |= v>>4
        v |= v>>8
        v |= v>>16
        v+=1
        return v

if __name__ == '__main__':
    init = NextPower2()
    print(init.next_pow2(3)) #4
    print(init.next_pow2(21)) #32
