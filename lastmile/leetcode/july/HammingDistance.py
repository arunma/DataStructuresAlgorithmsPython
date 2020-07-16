class HammingDistance:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        while x or y:
            if (x & 1 and not(y & 1)) or (y & 1 and not(x & 1)) :
                count+=1
            x=x>>1
            y=y>>1
        return count





if __name__ == '__main__':
    init = HammingDistance()
    print(init.hammingDistance(1, 4)) #2
    print(init.hammingDistance(1, 100001)) #2
