from typing import List

class KokoEatingBananas:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def isPossibleWithSpeed(speed):
            count=0
            for pile in piles:
                if pile>=speed:
                    count+=pile//speed
                if pile %speed!=0:
                    count+=1
            return count<=H


        low=1
        high=max(piles)
        while low<=high:
            mid=low+(high-low)//2
            if isPossibleWithSpeed(mid):
                high=mid-1
            else:
                low=mid+1
        return low




if __name__ == '__main__':
    init = KokoEatingBananas()
    print(init.minEatingSpeed(piles = [3,6,7,11], H = 8)) #4
    print(init.minEatingSpeed(piles = [30,11,23,4,20], H = 5)) #30
