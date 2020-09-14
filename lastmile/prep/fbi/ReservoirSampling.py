import random
import sys


class ReservoirSampling:

    def maxRandomIndex(self, arr):
        maxValue=-sys.maxsize
        maxIndex=-1
        count=0
        for i, num in enumerate(arr):
            if num>maxValue:
                maxValue=num
                maxIndex=i
                count=1
            elif num==maxValue:
                count+=1
                if random.randrange(count)==0:
                    maxIndex=i
            print (maxIndex)
        return maxIndex



if __name__ == '__main__':
    init = ReservoirSampling()
    print(init.maxRandomIndex([11, 30, 2, 30, 30, 30, 6, 2, 62, 62]))
