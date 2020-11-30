import random
from collections import Counter


class MaximumOccuringElementEqualProbability:

    def findRandomIndexOfMax(self, arr, n):
        counter=Counter(arr)

        maxItem=-1
        maxCount=0
        for num,cnt in counter.items():
            if cnt>maxCount:
                maxItem=num
                maxCount=cnt

        print (maxItem)

        indexList=[]
        for i, num in enumerate(arr):
            if num==maxItem:
                indexList.append(i)


        randIndex = random.randrange(len(indexList))
        return indexList[randIndex]


if __name__ == '__main__':
    arr = [-1, 4, 9, 7, 7, 2, 7, 3, 0, 9, 6, 5, 7, 8, 9]
    init = MaximumOccuringElementEqualProbability()
    n = len(arr)
    print(init.findRandomIndexOfMax(arr, n))


